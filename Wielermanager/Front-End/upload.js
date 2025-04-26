// DOM elements
const dropArea = document.querySelector('.file-action-card:first-of-type');
const selectFileBtn = dropArea.querySelector('.action-button');
const downloadBtn = document.querySelector('.file-action-card:nth-of-type(2) .action-button');
const fileInput = document.createElement('input');

// Set Flask server URL - adjust this to match your Flask server address
const FLASK_SERVER_URL = 'http://127.0.0.1:5000';

// Set up hidden file input
fileInput.type = 'file';
fileInput.accept = '.txt,.mp3,.pdf,.doc,.docx';
fileInput.style.display = 'none';
document.body.appendChild(fileInput);

// Add event listeners for drag and drop functionality
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

// Highlight drop area when file is dragged over
['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight() {
  dropArea.classList.add('highlight');
}

function unhighlight() {
  dropArea.classList.remove('highlight');
}

// Handle file drop
dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
  const dt = e.dataTransfer;
  const files = dt.files;
  handleFiles(files);
}

// Handle file selection via button
selectFileBtn.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', function() {
  handleFiles(this.files);
});

function handleFiles(files) {
  if (files.length === 0) return;
  
  const file = files[0];
  
  // Check file type by extension
  const fileName = file.name.toLowerCase();
  const validExtensions = ['.txt', '.mp3', '.pdf', '.doc', '.docx'];
  let isValid = false;
  
  for (const ext of validExtensions) {
    if (fileName.endsWith(ext)) {
      isValid = true;
      break;
    }
  }
  
  if (!isValid) {
    alert('Please upload only .txt, .mp3, .pdf, .doc, or .docx files');
    return;
  }
  
  // Check file size (50MB = 52428800 bytes)
  if (file.size > 52428800) {
    alert('File size exceeds 50MB limit');
    return;
  }
  
  // Show file name in the UI
  dropArea.querySelector('.file-action-title').textContent = `File selected: ${file.name}`;
  
  // Upload the file
  uploadFile(file);
}

async function uploadFile(file) {
  const formData = new FormData();
  formData.append('file', file);
  
  try {
    // Show loading state
    selectFileBtn.textContent = 'Uploading...';
    selectFileBtn.disabled = true;
    
    // Use the Flask server URL
    const response = await fetch(`${FLASK_SERVER_URL}/upload`, {
      method: 'POST',
      body: formData,
      // Include this to allow cross-origin requests
      mode: 'cors',
      credentials: 'same-origin'
    });
    
    console.log('Response status:', response.status);
    
    if (!response.ok) {
      throw new Error(`Upload failed with status: ${response.status}`);
    }
    
    const result = await response.json();
    console.log('File uploaded successfully:', result);
    
    // Reset button state
    selectFileBtn.innerHTML = '<svg class="button-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14 10V12.6667C14 13.0203 13.8595 13.3594 13.6095 13.6095C13.3594 13.8595 13.0203 14 12.6667 14H3.33333C2.97971 14 2.64057 13.8595 2.39052 13.6095C2.14048 13.3594 2 13.0203 2 12.6667V10M11.3333 5.33333L8 2M8 2L4.66667 5.33333M8 2V10" stroke="#F5F5F5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg><span>Select File</span>';
    selectFileBtn.disabled = false;
    
    // Enable download button when file is processed
    if (result.status === 'success' && result.processed_file) {
      downloadBtn.disabled = false;
      downloadBtn.onclick = () => {
        window.location.href = `${FLASK_SERVER_URL}/download/${result.processed_file}`;
      };
    }
  } catch (error) {
    console.error('Error uploading file:', error);
    alert('Error uploading file. Please try again.');
    
    // Reset button state
    selectFileBtn.innerHTML = '<svg class="button-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14 10V12.6667C14 13.0203 13.8595 13.3594 13.6095 13.6095C13.3594 13.8595 13.0203 14 12.6667 14H3.33333C2.97971 14 2.64057 13.8595 2.39052 13.6095C2.14048 13.3594 2 13.0203 2 12.6667V10M11.3333 5.33333L8 2M8 2L4.66667 5.33333M8 2V10" stroke="#F5F5F5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg><span>Select File</span>';
    selectFileBtn.disabled = false;
  }
}

// Debugging logs
console.log('Upload script loaded');
console.log('Drop area:', dropArea);
console.log('Flask server URL:', FLASK_SERVER_URL);

// Initialize download button as disabled
downloadBtn.disabled = true;