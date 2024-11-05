const delay = (duration) => new Promise(resolve => setTimeout(resolve, duration));
class ApiClient {
  #config = '';
  constructor() {
    this.#config = this.#loadConfig();
  }
  async #loadConfig() {
    try {
      const response = await fetch('config.json');
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      return await response.json();
    } catch (error) {
      console.error('Error loading configuration:', error.message);
    }
  }
  #mockFetchCategories() {
    return {
      "categories": [
        { "Id": 1, "name": "Category 1" },
        { "Id": 2, "name": "Category 2" },
        { "Id": 3, "name": "Category 3" }
      ]
    };
  }
  #mockFetchFlashcards() {
    return {
      "flashcards": [
        {
          "question": "What is your favorite season?",
          "correctAnswer": "Spring",
          "incorrectAnswers": [
            "Summer",
            "Fall",
            "Winter"
          ]
        },
        {
          "question": "What is your favorite animal?",
          "correctAnswer": "Dog",
          "incorrectAnswers": [
            "Cat",
            "Bird",
            "Cow"
          ]
        }
      ]
    }
  }
  async fetchCategories() {
    try {
      const host = (await this.#config)?.host;
      if (!host) {
        throw new Error('Host not found in configuration file.');
      }
      const mock = (await this.#config)?.mock;
      if (mock) {
        await delay(2000);
        return this.#mockFetchCategories();
      }
      const url = `${host}categories`;
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      return await response.json();
    } catch (error) {
      console.error(error);
      throw new Error('Error fetching categories. Error message: ' + error.message);
    }
  }
  async fetchFlashcards(categoryId, maxItems) {
    try {
      const host = (await this.#config)?.host;
      if (!host) {
        throw new Error('Host not found in configuration file.');
      }
      if (typeof categoryId !== 'number' || !Number.isInteger(categoryId) || categoryId <= 0) {
        throw new Error('Invalid categoryId: must be a positive integer.');
      }
      if (typeof maxItems !== 'number' || !Number.isInteger(maxItems) || maxItems <= 0) {
        throw new Error('Invalid maxItems: must be a positive integer.');
      }
      const mock = (await this.#config)?.mock;
      if (mock) {
        await delay(2000);
        return this.#mockFetchFlashcards();
      }
      const url = `${host}flashcards?categoryId=${categoryId}&maxItems=${maxItems}`;
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      return await response.json();
    } catch (error) {
      console.error(error);
      throw new Error('Error fetching flashcards. Error message: ' + error.message);
    }
  }
}
class ProgressHelper {
  showProgress() {
    const progressContainer = document.getElementById('progressContainer');
    if (progressContainer) {
      const progressModal = document.createElement('div');
      progressModal.id = 'progressModal';
      Object.assign(progressModal.style, {
        position: 'fixed',
        top: '0',
        left: '0',
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(128, 128, 128, 0.5)',
        zIndex: '9999',
        display: 'block'
      });
      const progressIndicator = document.createElement('div');
      progressIndicator.id = 'progressIndicator';
      Object.assign(progressIndicator.style, {
        position: 'absolute',
        bottom: '0',
        height: '10px',
        width: '100%'
      });
      const progress = document.createElement('div');
      progress.className = 'progress';
      Object.assign(progress.style, {
        borderRadius: '0'
      });
      const progressBar = document.createElement('div');
      progressBar.className = 'progress-bar progress-bar-striped progress-bar-animated';
      progressBar.setAttribute('role', 'progressbar');
      Object.assign(progressBar.style, {
        width: '100%',
        borderRadius: '0'
      });
      progress.appendChild(progressBar);
      progressIndicator.appendChild(progress);
      progressModal.appendChild(progressIndicator);
      progressContainer.appendChild(progressModal);
      document.body.style.pointerEvents = 'none'
    }
  }
  hideProgress() {
    const progressModal = document.getElementById('progressModal');
    if (progressModal) {
      progressModal.remove();
    }
    document.body.style.pointerEvents = '';
  }
}
class ErrorHandler {
  constructor() {
    this.errorContainer = document.getElementById('errorContainer');
  }
  showError(errorMessage) {
    const alertDiv = document.createElement('div');
    alertDiv.innerHTML = `
          <div class="alert border-2 border-end-0 border-start-0 alert-danger alert-dismissible fade show mb-0" role="alert" style="border-radius: 0;">
              ${errorMessage}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>`;
    alertDiv.style.borderRadius = 0;
    this.errorContainer.appendChild(alertDiv);
    setTimeout(() => {
      this.#hideAlert(alertDiv);
    }, 5000);
    const closeButton = alertDiv.querySelector('.btn-close');
    closeButton.addEventListener('click', () => {
      this.#hideAlert(alertDiv);
    });
  }
  hideErrors() {
    const alerts = this.errorContainer.querySelectorAll('.alert');
    alerts.forEach(alert => {
      this.#hideAlert(alert);
    });
  }
  #hideAlert(alertDiv) {
    if (alertDiv) {
      alertDiv.classList.remove('show');
      setTimeout(() => {
        alertDiv.remove();
      }, 500);
    }
  }
}