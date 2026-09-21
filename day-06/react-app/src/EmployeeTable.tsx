// Define and export the Employee interface directly from this file
export interface Employee {
    id: number;
    name: string;
    department: string;
    salary: number;
  }
  
  interface Props {
    employees: Employee[];
    onDelete: (id: number) => void;
  }
  
  export default function EmployeeTable({ employees, onDelete }: Props) {
    if (employees.length === 0) return <p>No employees match your search.</p>;
  
    return (
      <table style={{ width: '100%', textAlign: 'left', borderCollapse: 'collapse', marginTop: '1rem' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid #ccc' }}>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Salary</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(emp => (
            <tr key={emp.id} style={{ borderBottom: '1px solid #eee' }}>
              <td style={{ padding: '0.5rem 0' }}>{emp.id}</td>
              <td>{emp.name}</td>
              <td>{emp.department}</td>
              <td>₹{emp.salary.toLocaleString('en-IN')}</td>
              <td>
                <button onClick={() => onDelete(emp.id)} style={{ color: 'red', cursor: 'pointer' }}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  }