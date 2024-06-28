import streamlit as st
import summarization_lib as glib

st.set_page_config(layout="wide", page_title="Document Summarization")
st.title("Document Summarization")

@st.cache_resource #this decorator causes Streamlit to automatically cache the returned value
def get_download_file():
    return glib.get_example_file_bytes()


download_button = st.download_button(
    label="Download example PDF to upload",
    data=get_download_file(),
    file_name="summarization_example.pdf",
    mime="application/pdf"
)

uploaded_file = st.file_uploader("Select a PDF", type=['pdf'])

upload_button = st.button("Upload", type="primary")

if upload_button:
    with st.spinner("Uploading..."):

        upload_response = glib.save_file(file_bytes=uploaded_file.getvalue())

        st.success(upload_response)
        
        st.session_state.has_document = True

if 'has_document' in st.session_state: #see if document has been uploaded
    
    return_intermediate_steps = st.checkbox("Return intermediate steps", value=True)
    summarize_button = st.button("Summarize", type="primary")
    
    
    if summarize_button:
        st.subheader("Combined summary")

        with st.spinner("Running..."):
            response_content = glib.get_summary(return_intermediate_steps=return_intermediate_steps)


        if return_intermediate_steps:

            st.write(response_content["output_text"])

            st.subheader("Section summaries")

            for step in response_content["intermediate_steps"]:
                st.write(step)
                st.markdown("---")

        else:
            st.write(response_content)

