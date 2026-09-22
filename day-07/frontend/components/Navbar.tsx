import Link from "next/link";

export default function Navbar() {
  return (
    <nav style={{ background: "#333", color: "#fff", padding: "1rem" }}>
      <ul style={{ display: "flex", gap: "20px", listStyle: "none", margin: 0 }}>
        <li>
          {/* Notice we use Link href instead of a href */}
          <Link href="/" style={{ color: "white", textDecoration: "none" }}>
            Home
          </Link>
        </li>
        <li>
          <Link href="/about" style={{ color: "white", textDecoration: "none" }}>
            About
          </Link>
        </li>
      </ul>
    </nav>
  );
}