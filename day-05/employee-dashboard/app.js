// State Management
let employees = [];

// DOM References
const tbody = document.getElementById("employee-tbody");
const searchInput = document.getElementById("search-input");
const filterDept = document.getElementById("filter-dept");
const sortSelect = document.getElementById("sort-select");
const totalCountEl = document.getElementById("total-count");
const avgSalaryEl = document.getElementById("avg-salary");

const formModal = document.getElementById("form-modal");
const employeeForm = document.getElementById("employee-form");
const formTitle = document.getElementById("form-title");
const formId = document.getElementById("form-id");
const formName = document.getElementById("form-name");
const formEmail = document.getElementById("form-email");
const formDepartment = document.getElementById("form-department");
const formRole = document.getElementById("form-role");
const formSalary = document.getElementById("form-salary");

const detailsModal = document.getElementById("details-modal");
const detailsBody = document.getElementById("details-body");

// 1. Fetch Initial Data using Async/Await & Fallback to LocalStorage
const loadEmployees = async () => {
  const cached = localStorage.getItem("employees");
  if (cached) {
    employees = JSON.parse(cached);
    render();
    return;
  }

  try {
    const res = await fetch("data.json");
    if (!res.ok) throw new Error(`HTTP error status: ${res.status}`);
    employees = await res.json();
    saveToStorage();
    render();
  } catch (err) {
    console.error("Error fetching data.json, initializing fallback:", err);
    employees = [
      { id: 1, name: "Aditi Verma", email: "aditi.v@example.com", department: "Engineering", role: "Full Stack Engineer", salary: 85000 },
      { id: 2, name: "Rajesh Kumar", email: "rajesh.k@example.com", department: "Operations", role: "Operations Manager", salary: 72000 }
    ];
    saveToStorage();
    render();
  }
};

const saveToStorage = () => {
  localStorage.setItem("employees", JSON.stringify(employees));
};

// 2. Filter, Search, and Sort Processors
const getProcessedEmployees = () => {
  const query = searchInput.value.trim().toLowerCase();
  const dept = filterDept.value;
  const sortMode = sortSelect.value;

  return employees
    .filter(emp => {
      const matchesSearch = 
        emp.name.toLowerCase().includes(query) ||
        emp.email.toLowerCase().includes(query) ||
        emp.role.toLowerCase().includes(query);
      const matchesDept = dept ? emp.department === dept : true;
      return matchesSearch && matchesDept;
    })
    .sort((a, b) => {
      switch (sortMode) {
        case "name-asc": return a.name.localeCompare(b.name);
        case "name-desc": return b.name.localeCompare(a.name);
        case "salary-asc": return a.salary - b.salary;
        case "salary-desc": return b.salary - a.salary;
        default: return 0;
      }
    });
};

// 3. Render Table & Metrics
const render = () => {
  const processed = getProcessedEmployees();

  // Metrics
  totalCountEl.textContent = processed.length;
  const totalSalary = processed.reduce((sum, e) => sum + Number(e.salary), 0);
  const avg = processed.length ? (totalSalary / processed.length).toFixed(0) : 0;
  avgSalaryEl.textContent = `₹${Number(avg).toLocaleString("en-IN")}`;

  // Table rows
  if (processed.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center;">No employees found</td></tr>`;
    return;
  }

  tbody.innerHTML = processed
    .map(emp => `
      <tr>
        <td>${emp.id}</td>
        <td><strong>${emp.name}</strong></td>
        <td>${emp.email}</td>
        <td>${emp.department}</td>
        <td>${emp.role}</td>
        <td>₹${Number(emp.salary).toLocaleString("en-IN")}</td>
        <td class="actions">
          <button class="btn btn-view" onclick="viewEmployee(${emp.id})">View</button>
          <button class="btn btn-edit" onclick="openEditModal(${emp.id})">Edit</button>
          <button class="btn btn-delete" onclick="deleteEmployee(${emp.id})">Delete</button>
        </td>
      </tr>
    `)
    .join("");
};

// 4. CRUD Operations
window.openAddModal = () => {
  formTitle.textContent = "Add New Employee";
  employeeForm.reset();
  formId.value = "";
  formModal.showModal();
};

window.openEditModal = (id) => {
  const emp = employees.find(e => e.id === id);
  if (!emp) return;
  formTitle.textContent = "Edit Employee";
  formId.value = emp.id;
  formName.value = emp.name;
  formEmail.value = emp.email;
  formDepartment.value = emp.department;
  formRole.value = emp.role;
  formSalary.value = emp.salary;
  formModal.showModal();
};

window.deleteEmployee = (id) => {
  if (confirm("Are you sure you want to delete this employee?")) {
    employees = employees.filter(e => e.id !== id);
    saveToStorage();
    render();
  }
};

window.viewEmployee = (id) => {
  const emp = employees.find(e => e.id === id);
  if (!emp) return;
  detailsBody.innerHTML = `
    <p><strong>ID:</strong> ${emp.id}</p>
    <p><strong>Name:</strong> ${emp.name}</p>
    <p><strong>Email:</strong> ${emp.email}</p>
    <p><strong>Department:</strong> ${emp.department}</p>
    <p><strong>Role:</strong> ${emp.role}</p>
    <p><strong>Salary:</strong> ₹${Number(emp.salary).toLocaleString("en-IN")}</p>
  `;
  detailsModal.showModal();
};

// Event Listeners
document.getElementById("add-employee-btn").addEventListener("click", window.openAddModal);
document.getElementById("form-cancel-btn").addEventListener("click", () => formModal.close());
document.getElementById("details-close-btn").addEventListener("click", () => detailsModal.close());

searchInput.addEventListener("input", render);
filterDept.addEventListener("change", render);
sortSelect.addEventListener("change", render);

employeeForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const id = formId.value ? Number(formId.value) : Date.now();
  const payload = {
    id,
    name: formName.value.trim(),
    email: formEmail.value.trim(),
    department: formDepartment.value,
    role: formRole.value.trim(),
    salary: Number(formSalary.value)
  };

  if (formId.value) {
    employees = employees.map(emp => (emp.id === id ? payload : emp));
  } else {
    employees.push(payload);
  }

  saveToStorage();
  formModal.close();
  render();
});

// Initialize on page load
loadEmployees();