# security groups

# 1. ALB Security Group
# allows inbound HTTP traffic from the internet
resource "aws_security_group" "alb" {
  name        = "${var.project_name}-alb-sg"
  description = "Allow HTTP inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "HTTP from anywhere"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-alb-sg"
  }
}

# 2. ECS Service Security Group
# allows inbound traffic ONLY from the ALB
resource "aws_security_group" "ecs_service" {
  name        = "${var.project_name}-ecs-service-sg"
  description = "Allow inbound traffic from ALB"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "HTTP from ALB"
    from_port        = 5000 # flask app runs on this port
    to_port          = 5000
    protocol         = "tcp"
    security_groups  = [aws_security_group.alb.id] # IMPORTANT: Only allows traffic from the ALB
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-ecs-service-sg"
  }
}