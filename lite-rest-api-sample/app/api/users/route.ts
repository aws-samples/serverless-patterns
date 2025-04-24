import { NextRequest, NextResponse } from "next/server";

export function GET(request: NextRequest): NextResponse {
  const params = request.nextUrl.searchParams;
  const query = params.get("query");
  console.log(`GET /users query=${query}`);

  return NextResponse.json(
    { message: `GET /users query=${query}` },
    { status: 200 },
  );
}

export async function POST(request: NextRequest): Promise<NextResponse> {
  const params = await request.json();
  console.log(`POST /users body=${JSON.stringify(params)}`);

  return NextResponse.json(
    { message: `POST /users body=${JSON.stringify(params)}` },
    { status: 201 },
  );
}
