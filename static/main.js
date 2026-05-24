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

// ── Task management ──
const taskDataEls = document.querySelectorAll('.task-data')
const taskSearchEl = document.getElementById('task-search')

const allTasks = Array.from(taskDataEls).map(el => ({
  id: el.dataset.id,
  name: el.dataset.name,
  subject: el.dataset.subject,
  date: el.dataset.date,
  time: el.dataset.time,
  priority: el.dataset.priority,
  status: el.dataset.status,
}))

console.log('taskSearchEl:', taskSearchEl)
console.log('allTasks:', allTasks)

function filterTasks() {
  if (!taskSearchEl) return;

  const input = taskSearchEl.value.trim().toLowerCase();
  const dropdown = document.getElementById('task-dropdown');
  const deleteWrap = document.getElementById('delete-wrap');

  taskSearchEl.style.borderColor = '#ddd';

  if (!input) {
    dropdown.style.display = 'none';
    dropdown.innerHTML = '<option value="">-- Select a task --</option>';
    if (deleteWrap) deleteWrap.style.display = 'none';
    resetForm();
    return;
  }

  const matches = allTasks.filter(t =>
    (t.name || '').toLowerCase().includes(input) ||
    (t.subject || '').toLowerCase().includes(input)
  );

  if (matches.length === 0) {
    dropdown.style.display = 'none';
    taskSearchEl.style.borderColor = 'crimson';
    return;
  }

  dropdown.innerHTML = `<option value="">-- Matches found (${matches.length}) --</option>`;
  matches.forEach(t => {
    const opt = document.createElement('option');
    opt.value = t.id;
    opt.textContent = `${t.name} — ${t.subject}`;
    dropdown.appendChild(opt);
  });

  dropdown.style.display = 'block';

  // Auto-select first match
  dropdown.value = matches[0].id;
  selectTask(matches[0].id);
}

// Add this listener so the form fills when a dropdown item is picked
const taskDropdown = document.getElementById('task-dropdown');
if (taskDropdown) {
  taskDropdown.addEventListener('change', (e) => {
    if (e.target.value) {
      selectTask(e.target.value);
    }
  });
}


function selectTask(id) {
  if (!id) return
  const task = allTasks.find(t => t.id === id)
  if (!task) return

  const formTitle = document.getElementById('form-title')
  const taskId = document.getElementById('task-id')
  if (formTitle) formTitle.innerText = "✎ Edit Task"
  if (taskId) taskId.value = task.id
  if (document.getElementById('f-name')) document.getElementById('f-name').value = task.name
  if (document.getElementById('f-subject')) document.getElementById('f-subject').value = task.subject
  if (document.getElementById('f-date')) document.getElementById('f-date').value = task.date
  if (document.getElementById('f-time')) document.getElementById('f-time').value = task.time
  if (document.getElementById('f-priority')) document.getElementById('f-priority').value = task.priority
  if (document.getElementById('f-status')) document.getElementById('f-status').value = task.status
  if (document.getElementById('submit-btn')) document.getElementById('submit-btn').innerText = "Update Task"
  if (document.getElementById('delete-task-id')) document.getElementById('delete-task-id').value = task.id
  if (document.getElementById('delete-wrap')) document.getElementById('delete-wrap').style.display = 'block'

  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function resetForm() {
  const formTitle = document.getElementById('form-title')
  const taskForm = document.getElementById('task-form')
  const submitBtn = document.getElementById('submit-btn')
  const deleteWrap = document.getElementById('delete-wrap')
  const dropdown = document.getElementById('task-dropdown')
  const taskSearch = document.getElementById('task-search')
  const taskId = document.getElementById('task-id')

  if (formTitle) formTitle.innerText = "＋ Add New Task"
  if (taskForm) taskForm.reset()
  if (submitBtn) submitBtn.innerText = "Save Task"
  if (deleteWrap) deleteWrap.style.display = 'none'
  if (dropdown) dropdown.style.display = 'none'
  if (taskSearch) taskSearch.value = ''
  if (taskId) taskId.value = ''
}

// ── Homework filter ──
function filterHomework() {
  const val = document.getElementById('hw-filter').value
  document.querySelectorAll('#hw-body tr').forEach(tr => {
    if (val === 'All') { tr.style.display = ''; return }
    tr.style.display = (tr.dataset.when === val.toLowerCase()) ? '' : 'none'
  })
}

// ── Enter key triggers search ──
if (taskSearchEl) {
  taskSearchEl.addEventListener('input', filterTasks);
  taskSearchEl.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') e.preventDefault()
  })
}