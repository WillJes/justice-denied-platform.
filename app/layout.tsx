import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {title:"Justice Denied | Official Film Platform",description:"The official home of Justice Denied, an independent documentary by Jestina Weems-Rosenduft.",icons:{icon:"/favicon.svg"}};
export default function RootLayout({children}:{children:React.ReactNode}) {return <html lang="en"><body>{children}</body></html>}
