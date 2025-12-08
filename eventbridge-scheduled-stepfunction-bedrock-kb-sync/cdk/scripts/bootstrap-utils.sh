#!/bin/bash
# This script contains bash common platform setup bash functions.
# Current Release: 0.1
# Release Date: 2024-04-27

bootstrap_util() {
    local project_bootstrap_command script_path script_dir project_dir project_name base_dir python_install_dir green red yellow blue reset 
    project_bootstrap_command="$1"
    shift
   

    # Store Useful Directories in Variables
    script_path=$(realpath "${BASH_SOURCE[0]}")
    script_dir="$(dirname "${script_path}")"
    project_dir="$(dirname "${script_dir}")"
    project_name="$(basename "${project_dir}")"
    base_dir=$(dirname "${project_dir}")
    
    # Set some ASCII Colors
    SECONDS=0
    green="\033[0;32m"
    red="\033[0;31m"
    yellow="\033[0;33m"
    reset="\033[0m"
    blue="\033[0;34m"

    # shellcheck disable=SC2317
    echo_time_to_complete(){
        # Print out the time the current Action took
        if (( SECONDS > 60 )) ; then
            local minutes seconds
            minutes=$((SECONDS/60))
            seconds=$((SECONDS%60))
            echo "[Completed in ${minutes} minute(s) and ${seconds} second(s)]"
        else
            echo "[Completed in ${SECONDS} seconds]"
        fi
        SECONDS=0
    }
    # shellcheck disable=SC2317
    echo_pip_version(){
        # Prints the version of a pip module without the additional bloat.
        local pip_module_name module_version
        pip_module_name="$1"
        module_version="$(pip show "${pip_module_name}" | grep 'Version:' | cut -d ' ' -f 2)"
        echo -e "  ↳ Using ${green}${pip_module_name}${reset} ${module_version}"
    }

    # shellcheck disable=SC2317
    validate_external_project_dependencies(){
        # Validate that the required external dependencies are installed in the base directory,
        # Read the entries in the file .external_project_dependencies and print a warning if any project is missing.
        local project_dependencies_file_path
        project_dependencies_file_path="${project_dir}/.external_project_dependencies"
        
        if [[ -f "${project_dependencies_file_path}" ]]; then
            # Count the entries in the dependency file
            line_count=$(wc -l < "${project_dependencies_file_path}")
            # Remove all whitespace from the line count
            line_count="${line_count//[[:space:]]/}"
            echo "🔎 ${line_count} External Project Dependencies defined in .external_project_dependencies."
            # Read the entries in the file .external_project_dependencies
            while read -r entry; do
                if ! [[ -d "${base_dir}/${entry}" ]]; then
                    echo -e "  ↳ ${red}❗️ Project Dependency: ${entry} not present.${reset}"
                else
                    echo -e "  ↳ ${green}✅ Project Dependency: ${entry} present.${reset}"
                fi      
            done < "${project_dependencies_file_path}"
        fi
    }

    # shellcheck disable=SC2317
    setup_python_runtime(){
        # Ensure a specific Python version is installed and set as global then create a new virtual Environment for it.
        # A single argument is accepted which is the version of Python to install.
        local default_python_version="3.9.18"
        local target_python_version="${1:-${default_python_version}}"
        echo "🗑️  Removing Existing .venv"
        rm -rf .venv
        echo "🐍 Setting Python version to Python ${target_python_version}"
        if command -v pyenv &> /dev/null; then
            local pyenv_versions
            pyenv_versions=$(pyenv versions --bare)
            if echo "${pyenv_versions}" | grep -q ^"${target_python_version}"; then
                echo -e " ↳ ${green}Python ${target_python_version} already installed${reset}"
            else
                echo " ↳ Installing Python ${target_python_version}"
                pyenv install "${target_python_version}"
            fi
            pyenv global "${target_python_version}"
            echo "🐍 Creating python Virtual Environment"
            python3 -m venv .venv
            # shellcheck disable=SC2086
            # shellcheck source=/dev/null
            source .venv/bin/activate
            python_install_dir=$(command -v python3)
            echo "🐍 Which Python: ${python_install_dir}"
        else
            echo "🚨 pyenv not installed"
            echo " ↳ Please install pyenv and try again"
            exit 1
        fi
    }   
    # shellcheck disable=SC2317
    upgrade_pip_version(){
        # Upgrade pip to the latest version
        echo -n "🐍 Upgrading Pip... "
        python -m pip install -q -U pip
        echo_time_to_complete
        echo_pip_version pip
    }

    # shellcheck disable=SC2317
    setup_adf_build_path(){
        # Check if the variable ADF_BUILD_DIRECTORY exists then use that
        local shared_dir="aws-deployment-framework-bootstrap/adf-build/shared"
        local adf_path_list=()
        if [[ -n ${ADF_BUILD_HOME} ]]; then
            echo -e "${yellow} 🪄 Detected ADF_BUILD_HOME environment variable: ${ADF_BUILD_HOME} ${reset}"
            # If set, use it as the first path in the list
            adf_path_list=("${ADF_BUILD_HOME}")
        fi
        adf_path_list+=("${base_dir}/${shared_dir}" "${base_dir}/adf-dev/${shared_dir}")
        for adf_path in "${adf_path_list[@]}"; do
            if [[ -d "${adf_path}" ]]; then
                echo "✅ Setting venv activate script to automatically append ${adf_path} to PYTHONPATH during venv activation"
                cat >> .venv/bin/activate << EOL
if [ -n "\${PYTHONPATH}" ]; then
    if ! echo "\${PYTHONPATH}" | grep -q "${adf_path}"; then
        export PYTHONPATH="\${PYTHONPATH}:${adf_path}"
    fi
fi
EOL
                return 0                
            else
                echo "❗️ Warning: ADF Bootstrap directory: ${adf_path} not found!"
            fi
        done
        echo -e "⛔️ ${red} Error: This Project has dependencies on modules in the ADF-Bootstrap Repository. ${reset}"
        echo -e "${red} To fix this, please define the path to adf-build/shared via ADF_BUILD_HOME environment variable.${reset}"
        exit 1    
    }

    # shellcheck disable=SC2317
    install_common_tools(){
        SECONDS=0
        DEFAULT_COMMON_TOOLS=(
            pip-tools
            setuptools
            pep8
            pre-commit
            cfn-lint
            cdk-nag
            commitizen
            bandit
            pip-audit
        )
        local common_tools="${1:-${DEFAULT_COMMON_TOOLS[*]}}"
        # Install all common packages with a single pip install command
        echo -n "🐍 Installing Common Tools... "
        # shellcheck disable=SC2086
        pip install -q ${common_tools}
        echo_time_to_complete
        # Print a message for each package
        for tool in ${common_tools}; do
            echo_pip_version "${tool}"
        done
    }

    # shellcheck disable=SC2317
    install_python_dependencies(){
        # Install the Python Dependencies
        declare -a DEFAULT_REQUIREMENTS_FILES=(
            "Project requirements"
        )
        # Use input or default_requirements_files if not set
        local -a req_files=("${@:-${DEFAULT_REQUIREMENTS_FILES[@]}}")
        for dependency in "${req_files[@]}"; do
            dependency_label="${dependency%% *}"  
            requirements_file="${dependency##* }"
            if [[ -f "${requirements_file}.in" ]]; then
                echo -n "🐍 Compiling ${dependency_label} Requirements... "
                pip-compile -q --output-file="${requirements_file}.txt" "${requirements_file}.in" --strip-extras
                echo_time_to_complete
            else
                echo -e "${red}❗️ ${requirements_file}.in not found... checking for ${requirements_file}.txt ${reset}"
            fi
            if [[ -f "${requirements_file}.txt" ]]; then
                echo -n "🐍 Installing ${dependency_label} Requirements... "
                pip install -q -r "${requirements_file}.txt" 
                echo_time_to_complete
                awk -F'==' '/^[^#]/ && NF>1 {printf " ↳ Using \033[0;32m%s\033[0m %s\n", $1, $2}' "${requirements_file}.txt"
            else 
                echo -e "${red}❗️ Error: ${requirements_file}.txt not found!${reset}"
            fi
        # Add your logic here to process the requirements file
        done
    }
     
    # shellcheck disable=SC2317
    install_node_dependencies(){
        # Install the Node Dependencies
        # Check if the node package.json exists
        if [[ -f "package.json" ]]; then
            if command -v node &> /dev/null; then
                echo -n "Installing Node Dependencies..."
                npm install
                echo "Done." 
            else 
                echo "🚨 node not installed"
                echo " ↳ Please install node and try again"
                exit 1
            fi
        else
            echo -e "${yellow} Node dependency isn't installed due to the absence of package.json within the repository....${reset}"
        fi
    }

    # shellcheck disable=SC2317
    length_of_string(){
        local input="$1"
        echo -n "${input}" | awk 'BEGIN {FS=""} {print NF}'
    }

    # shellcheck disable=SC2317
    bootstrap_message(){
         # Print a Simple Bootstrap Message with a blue border
        local message message_length dashes
        message="$1"
        length=$(length_of_string "${message}")
        message_length=$(seq 1 "${length}") 
        # splitting message_length is needed
        # shellcheck disable=SC2086
        dashes="$(printf "%0.s═" ${message_length})"
        #dashes=$(printf '%*s' "$length" '' | sed 's/ /═/g')
        echo -e "${blue}╒══${dashes}══╕\n│ ${reset}${message}${blue} │\n╘══${dashes}══╛${reset}"
    }
    # shellcheck disable=SC2317
    bootstrap_start(){
        # Print a Simple Starting Bootstrap Message
        bootstrap_message " 🚗  Bootstrapping Project: ${project_name} 🚗 "
    }

    # shellcheck disable=SC2317
    bootstrap_complete() {
        # Just a simple message to let the user know the bootstrap is complete
        bootstrap_message " 🏁 Bootstrap Project: ${project_name} Complete. 🏁 "
    }

    case "${project_bootstrap_command}" in
        "")
            # If no namespace is provided, list available functions
            function_list=$(typeset -F)
            grep_output=$(grep "^declare -f" <<< "${function_list}")
            echo "Available functions in bootstrap-utils:"
            echo "${grep_output//declare -f /}"
            ;;
        *)
            # If a namespace is provided, execute the requested function with arguments
            "${project_bootstrap_command}" "$@"
            ;;
    esac
}
