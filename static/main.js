// ── Password toggle ──
function setupToggle(btnId, fieldId) {
  const btn = document.querySelector('#' + btnId)
  if (!btn) return
  const icon = btn.querySelector('img')
  const field = document.querySelector('#' + fieldId)


  btn.addEventListener('click', () => {
    field.type = field.type === 'password' ? 'text' : 'password'
    icon.src = icon.src.includes('open')
      ? icon.src.replace('images/eye_open.svg', 'images/eye_closed.svg')
      : icon.src.replace('images/eye_closed.svg', 'images/eye_open.svg')
  })
}


const loginBtn = document.querySelector('#show-passwd')
if (loginBtn) setupToggle('show-passwd', 'password')


const signupBtn1 = document.querySelector('#show-passwd-1')
if (signupBtn1) {
  setupToggle('show-passwd-1', 'id_password')
  setupToggle('show-passwd-2', 'id_confirm_password')
}


lucide.createIcons();

function toggleSidebar() {
      const sidebar = document.querySelector('.sidebar');
      sidebar.classList.toggle('retracted');
      localStorage.setItem('sidebarRetracted', sidebar.classList.contains('retracted'));
    }


document.addEventListener("DOMContentLoaded", () => {
      if (localStorage.getItem('sidebarRetracted') === 'true') {
        document.querySelector('.sidebar').classList.add('retracted');
      }
    });


function switchTab(name, el) {
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      document.getElementById('tab-' + name).classList.add('active');
      el.classList.add('active');
    }

function toggleReport(btn) {
  const panel = document.getElementById('report-preview');
  const frame = document.getElementById('pdf-frame');
  const isHidden = panel.style.display === 'none' || panel.style.display === '';

  if (isHidden) {
    panel.style.display = 'block';
    btn.innerHTML = '<i data-lucide="eye-off" width="16" height="16" style="vertical-align:middle;margin-right:6px;"></i>Hide Preview';
    // Lazy-load: only set src the first time
    if (!frame.src || frame.src === window.location.href) {
      document.getElementById('pdf-loading').style.display = 'inline';
      frame.src = frame.dataset.src;
    }
  } else {
    panel.style.display = 'none';
    btn.innerHTML = '<i data-lucide="eye" width="16" height="16" style="vertical-align:middle;margin-right:6px;"></i>Preview Report';
  }
  lucide.createIcons();
}


function previewDocx(btn) {
    const container = document.getElementById('docx-preview-container');
    container.style.display = "block";
    container.innerHTML = "<p style='color:#78716C; font-style:italic;'>Processing document text formatting...</p>";

    const reportUrl = btn.dataset.url;

    fetch(reportUrl)
        .then(response => {
            if (!response.ok) throw new Error("Could not fetch report.");
            return response.arrayBuffer();
        })
        .then(arrayBuffer => {
            return mammoth.convertToHtml({ arrayBuffer: arrayBuffer });
        })
        .then(result => {
            container.innerHTML = result.value;
            if (result.messages.length > 0) {
                console.log("Mammoth warnings:", result.messages);
            }
            // Show the Print button now that preview is loaded
            document.getElementById('print-report-btn').style.display = 'inline-flex';
        })
        .catch(error => {
            console.error("Preview error:", error);
            container.innerHTML = "<p style='color:#b13535;'>Failed to load document preview.</p>";
        });
}

function printDocx() {
    const content = document.getElementById('docx-preview-container').innerHTML;
    const printWindow = window.open('', '_blank');
    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>SBA Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 2cm; font-size: 11pt; }
                table { border-collapse: collapse; width: 100%; }
                td, th { border: 1px solid #ccc; padding: 4px 8px; }
                @media print { body { margin: 1.5cm; } }
            </style>
        </head>
        <body>${content}</body>
        </html>
    `);
    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
}