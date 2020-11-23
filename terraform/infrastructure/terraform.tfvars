env = {
  default = {

    ecs = {
      app_count                            = 1
      instance_type = "t2.micro"
      autoscaling_policy_name              = "ecs_autoscaling"
      autoscaling_request_per_target_value = "250"
      health_check_path                    = "/health_check"
      healthy_threshold                    = "5"
      unhealthy_threshold                  = "2"
      health_check_interval                = "30"
      health_check_timeout                 = "5"
      min_capacity                         = 1
      max_capacity                         = 3

    }

    network = {
      route53_zone = "ayataxim.me"
    }

    task = {
      ecs_task_execution_role_name = "EcsTaskExecutionRole"
      registry_name                = "taximecr"
      app_image                    = "latest"
      cpu                  = "256"
      memory               = "1024"
    }

    certificate_route53 = {
      certificate_domain = "api.ayataxim.me"
    }

    website = {
      bucket_name = "ayataxim.me"
      domain_name = "ayataxim.me"
    }

    app_port       = 8000
    aws_region     = "eu-central-1"
    project_name   = "taxim"
    stage = "dev"

  }

  master = {

    ecs = {
      app_count                            = 1
      instance_type = "t2.micro"
      autoscaling_policy_name              = "ecs_autoscaling"
      autoscaling_request_per_target_value = "250"
      health_check_path                    = "/health_check"
      healthy_threshold                    = "5"
      unhealthy_threshold                  = "2"
      health_check_interval                = "30"
      health_check_timeout                 = "5"
      min_capacity                         = 1
      max_capacity                         = 3

    }

    network = {
      route53_zone = "ayataxim.me"
    }

    task = {
      ecs_task_execution_role_name = "EcsTaskExecutionRole"
      registry_name                = "taximecr"
      app_image                    = "latest"
      cpu                  = "256"
      memory               = "1024"
    }

    certificate_route53 = {
      certificate_domain = "api.ayataxim.me"
    }

    website = {
      bucket_name = "ayataxim.me"
      domain_name = "ayataxim.me"
    }

    app_port       = 8000
    aws_region     = "eu-central-1"
    project_name   = "taxim"
    stage = "prod"

  }
}
