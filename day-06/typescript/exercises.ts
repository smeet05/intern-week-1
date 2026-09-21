// Primitive types and Union types
let employeeName: string = "Rahul";
let isActive: boolean = true;
let department: "Engineering" | "HR" | "Finance" = "Engineering";

// Interfaces and Optional properties
interface Employee {
  id: number;
  name: string;
  salary: number;
  role?: string;
}

// Type aliases and Arrays
type EmployeeList = Employee[];
const staff: EmployeeList = [
  { id: 1, name: "Rahul", salary: 50000, role: "Developer" }
];

// Functions and Type narrowing
function getSalaryDisplay(salary: number | string): string {
  if (typeof salary === "number") {
    return `₹${salary.toLocaleString()}`; // Type narrowing: TypeScript knows it's a number here
  }
  return salary;
}

// Generics
function getFirstElement<T>(items: T[]): T | undefined {
  return items.length > 0 ? items[0] : undefined;
}