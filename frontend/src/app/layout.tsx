// import type { Metadata } from "next";
// import { Inter, Poppins, Source_Sans_3 } from "next/font/google";
// import "../styles/globals.css";
// import { NavigationProvider } from "@/contexts/NavigationContext";
// import { ExpandableCardProvider } from "@/contexts/ExpandableCardContext";
// import { Sidebar, RightSidebar } from "@/components/layout";
// import { ContentSwitcher } from "@/components/layout/ContentSwitcher";

// const inter = Inter({
//   variable: "--font-inter",
//   subsets: ["latin"],
// });

// const poppins = Poppins({
//   variable: "--font-poppins",
//   subsets: ["latin"],
//   weight: ["300", "400", "500", "600", "700"],
// });

// const sourceSans = Source_Sans_3({
//   variable: "--font-source-sans",
//   subsets: ["latin"],
// });

// export const metadata: Metadata = {
//   title: "Modular Next.js App",
//   description:
//     "A modular Next.js application with Tailwind CSS and dark blue theme",
// };

// export default function RootLayout({
//   children,
// }: Readonly<{
//   children: React.ReactNode;
// }>) {
//   return (
//     <html lang="en" className="dark">
//       <body
//         className={`${inter.variable} ${poppins.variable} ${sourceSans.variable} antialiased min-h-screen bg-black flex justify-center text-white font-sans`}
//         style={{
//           fontFamily: 'var(--font-inter), -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
//         }}
//       >
//         <NavigationProvider>
//           <ExpandableCardProvider>
//             <div className="min-h-screen bg-black flex w-full">
//               <Sidebar />
//               <ContentSwitcher />
//               <RightSidebar />
//             </div>
//           </ExpandableCardProvider>
//         </NavigationProvider>
//       </body>
//     </html>
//   );
// }
