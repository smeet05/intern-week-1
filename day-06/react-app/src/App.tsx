import React, { useState, useEffect } from 'react';
import EmployeeTable, { type Employee } from './EmployeeTable';

export default function App() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [search, setSearch] = useState('');
  const [filterDept, setFilterDept] = useState('');

  // Form State
  const [name, setName] = useState('');
  const [dept, setDept] = useState('Engineering');
  const [salary, setSalary] = useState('');

  // Initialize data from LocalStorage on mount
  useEffect(() => {
    const cached = localStorage.getItem('react-dashboard-data');
    if (cached) {
      setEmployees(JSON.parse(cached));
    } else {
      setEmployees([{ id: 1, name: 'Ananya', department: 'Engineering', salary: 85000 }]);
    }
  }, []);

  // Save to LocalStorage whenever employees state changes
  useEffect(() => {
    localStorage.setItem('react-dashboard-data', JSON.stringify(employees));
  }, [employees]);

  // Derived State for Metrics & Filtering
  const filteredEmployees = employees.filter(emp => {
    const matchesSearch = emp.name.toLowerCase().includes(search.toLowerCase());
    const matchesDept = filterDept ? emp.department === filterDept : true;
    return matchesSearch && matchesDept;
  });

  const totalEmployees = filteredEmployees.length;
  const avgSalary = totalEmployees > 0 
    ? filteredEmployees.reduce((sum, emp) => sum + emp.salary, 0) / totalEmployees 
    : 0;

  // Event Handlers (Using React.FormEvent to fix the cutout error)
  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault();
    const newEmp: Employee = {
      id: Date.now(),
      name,
      department: dept,
      salary: Number(salary)
    };
    setEmployees([...employees, newEmp]);
    setName('');
    setSalary('');
  };

  const handleDelete = (id: number) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  return (
    <div style={{ maxWidth: '900px', margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>Employee Management Dashboard</h1>
      
      <div style={{ display: 'flex', gap: '2rem', background: '#f4f4f4', padding: '1rem', marginBottom: '1.5rem' }}>
        <div><strong>Total Employees:</strong> {totalEmployees}</div>
        <div><strong>Average Salary:</strong> ₹{Math.round(avgSalary).toLocaleString('en-IN')}</div>
      </div>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
        <input 
          type="text" 
          placeholder="Search by name..." 
          value={search} 
          onChange={e => setSearch(e.target.value)} 
          style={{ flex: 1, padding: '0.5rem' }}
        />
        <select value={filterDept} onChange={e => setFilterDept(e.target.value)} style={{ padding: '0.5rem' }}>
          <option value="">All Departments</option>
          <option value="Engineering">Engineering</option>
          <option value="HR">HR</option>
          <option value="Operations">Operations</option>
        </select>
      </div>

      <EmployeeTable employees={filteredEmployees} onDelete={handleDelete} />

      <div style={{ marginTop: '3rem', borderTop: '2px solid #ccc', paddingTop: '1rem' }}>
        <h3>Add New Employee</h3>
        <form onSubmit={handleAdd} style={{ display: 'flex', gap: '1rem' }}>
          <input required placeholder="Full Name" value={name} onChange={e => setName(e.target.value)} />
          <input required type="number" placeholder="Salary" value={salary} onChange={e => setSalary(e.target.value)} />
          <select value={dept} onChange={e => setDept(e.target.value)}>
            <option value="Engineering">Engineering</option>
            <option value="HR">HR</option>
            <option value="Operations">Operations</option>
          </select>
          <button type="submit" style={{ cursor: 'pointer', padding: '0.5rem 1rem' }}>Save Employee</button>
        </form>
      </div>
    </div>
  );
}