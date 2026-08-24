import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Justice Denied | Official Film Platform",
  description: "The official home of Justice Denied, an independent documentary by Jestina Weems-Rosenduft.",
  manifest: "/manifest.webmanifest",
  icons: {
    icon: "/favicon.svg",
    apple: "/images/justice-denied-cover-clean.jpg",
  },
  appleWebApp: {
    capable: true,
    title: "Justice Denied",
    statusBarStyle: "black-translucent",
  },
};

export default function RootLayout({children}:{children:React.ReactNode}) {
  return <html lang="en"><body>{children}</body></html>;
}
