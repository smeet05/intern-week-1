// Sample dataset for exercises
const employees = [
    { id: 1, name: "Aarav Sharma", department: "Engineering", salary: 75000, role: "Developer" },
    { id: 2, name: "Priya Patel", department: "HR", salary: 52000, role: "Recruiter" },
    { id: 3, name: "Rohan Gupta", department: "Engineering", salary: 90000, role: "Lead" },
    { id: 4, name: "Sneha Rao", department: "Marketing", salary: 61000, role: "Specialist" },
    { id: 5, name: "Vikram Singh", department: "HR", salary: 48000, role: "Coordinator" }
  ];
  
  // 1. map(): Extract employee names and roles
  const employeeDirectory = employees.map(({ name, role }) => `${name} - ${role}`);
  console.log("Directory:", employeeDirectory);
  
  // 2. filter(): Employees with salary >= 60000
  const highEarners = employees.filter(emp => emp.salary >= 60000);
  console.log("High Earners:", highEarners);
  
  // 3. reduce(): Calculate average salary
  const totalSalary = employees.reduce((acc, emp) => acc + emp.salary, 0);
  const averageSalary = totalSalary / employees.length;
  console.log("Average Salary:", averageSalary);
  
  // 4. find(): Find employee by ID
  const foundEmp = employees.find(emp => emp.id === 3);
  console.log("Found ID 3:", foundEmp);
  
  // 5. sort(): Sort employees by salary descending
  const sortedBySalary = [...employees].sort((a, b) => b.salary - a.salary);
  console.log("Sorted by Salary:", sortedBySalary);
  
  // 6. async/await with Promise demonstration
  const fetchMockData = async () => {
    try {
      const result = await new Promise((resolve) => {
        setTimeout(() => resolve("Async data successfully fetched!"), 500);
      });
      console.log(result);
    } catch (error) {
      console.error("Fetch failed:", error);
    }
  };
  fetchMockData();