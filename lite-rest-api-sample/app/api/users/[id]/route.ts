import { NextRequest, NextResponse } from "next/server";

export function GET(
  request: NextRequest,
  { params }: { params: { id: string } },
): NextResponse {
  console.log(`GET /users/${params.id} id=${params.id}`);
  return NextResponse.json(
    { message: `GET /users/${params.id} id=${params.id}` },
    { status: 200 },
  );
}

export function PUT(
  request: NextRequest,
  { params }: { params: { id: string } },
): NextResponse {
  console.log(`PUT /users/${params.id} id=${params.id}`);
  return new NextResponse(null, { status: 204 });
}

export function DELETE(
  request: NextRequest,
  { params }: { params: { id: string } },
): NextResponse {
  console.log(`DELETE /users/${params.id} id=${params.id}`);
  return new NextResponse(null, { status: 204 });
}
