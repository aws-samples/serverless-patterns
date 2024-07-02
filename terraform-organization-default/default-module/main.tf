
/* resource "aws_subnet" "example" {
  count             = 2
  vpc_id            = data.aws_vpc.vpc.id
  cidr_block        = cidrsubnet(data.aws_vpc.vpc.cidr_block, 4, count.index)
  availability_zone = element(["us-east-1a", "us-east-1b"], count.index)

  tags = {
    #Name = "example-subnet-${count.index}"
    Name = "example-subnet-${count.index}-${local.prefix}"
  }
} */
/*resource "aws_instance" "my_instance"{
  ami = var.ami
  instance_type = "t2.micro"
  subnet_id = aws_subnet.example[1].id

}*/
resource "null_resource" "example" {
}