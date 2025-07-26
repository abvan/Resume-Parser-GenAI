const fileInput = document.getElementById('file-input');
    const fileCounter = document.getElementById('file-counter');

    fileInput.addEventListener('change', function () {
      const fileCount = this.files.length;
      if (fileCount > 0) {
        fileCounter.textContent = `${fileCount} file${fileCount !== 1 ? 's' : ''} selected`;
        fileCounter.classList.add('show');
      } else {
        fileCounter.classList.remove('show');
      }
    });

    const fileUpload = document.querySelector('.file-upload');

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
      fileUpload.addEventListener(eventName, e => {
        e.preventDefault();
        e.stopPropagation();
      });
    });

    ['dragenter', 'dragover'].forEach(eventName => {
      fileUpload.addEventListener(eventName, () => {
        fileUpload.style.borderColor = '#0F5299';
        fileUpload.style.background = 'linear-gradient(135deg, rgba(145, 149, 214, 0.3), rgba(77, 177, 179, 0.3))';
      });
    });

    ['dragleave', 'drop'].forEach(eventName => {
      fileUpload.addEventListener(eventName, () => {
        fileUpload.style.borderColor = '#9195D6';
        fileUpload.style.background = 'linear-gradient(135deg, rgba(145, 149, 214, 0.1), rgba(77, 177, 179, 0.1))';
      });
    });

    fileUpload.addEventListener('drop', e => {
      const dt = e.dataTransfer;
      const files = dt.files;
      fileInput.files = files;

      const event = new Event('change', { bubbles: true });
      fileInput.dispatchEvent(event);
    });