import "./globals.css";
import Navbar from "../components/Navbar"; // <-- Import it here

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Navbar /> {/* <-- Place it above {children} */}
        {children}
      </body>
    </html>
  );
}