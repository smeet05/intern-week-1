# Day 5: Modern JavaScript & Asynchronous Programming

## Project Overview
This project focuses on modern ES6+ JavaScript concepts and building an interactive Employee Dashboard supporting full CRUD operations, dynamic filtering, sorting, searching, and asynchronous data fetching without third-party frameworks.

## Features
* **Read / List**: Fetches initial employee records via asynchronous `fetch()` API and displays them in a tabular layout.
* **Search**: Real-time multi-field search across employee name, email, and role.
* **Filter**: Department-level filtering using ES6 `filter()`.
* **Sort**: Multi-parameter sorting (Name A-Z/Z-A, Salary High/Low) using ES6 `sort()`.
* **Create & Update**: Modal dialog forms with inputs for adding new records or editing existing ones.
* **Delete**: Confirmation-guarded deletion logic.
* **Metrics**: Real-time recalculation of total staff and average salary using ES6 `reduce()`.
* **Persistence**: Synchronizes state updates to `localStorage`.

## Technology Stack
* Modern JavaScript (ES6+ arrow functions, destructuring, template literals, async/await, Array methods)
* HTML5 (Semantic elements, `<dialog>` modals)
* CSS3 (Flexbox, responsive styling)

## Challenges Faced & Solutions
* **CORS Restriction on Local Fetch**: Browsers block `fetch('data.json')` when opened via `file://`.
  * **Solution**: Served the files locally using `python -m http.server 8000` and incorporated a fallback to `localStorage` to ensure data persists.