import { NextRequest, NextResponse } from "next/server";

export function middleware(request: NextRequest) {
  console.log(`middleware path: ${request.nextUrl.pathname}`)
  return NextResponse.next();
}

export const config = {
  matcher: "/api/(.*)",
};
