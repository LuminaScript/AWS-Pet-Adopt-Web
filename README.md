## AdoptPal - Pet Adoption Management System
### Demo
Demo Video Link: [Google Drive Demo](https://drive.google.com/file/d/1_LMF4OyauoHJ737-mnlrSdqHWqAnU5bg/view?usp=drive_link)

### Introduction
AdoptPal simplifies pet adoption, connecting pet owners and adopters. It utilizes AWS for scalability and security.
1. **For Adopters:**
   - Register and authenticate via username, email, or Google SSO.
   - Browse available pets and receive email notifications for new ones.
2. **For Pet Owners:**
   - Register and authenticate via username, email, or Google SSO.
   - Manage pet listings, including updates and notifications.

### Personas and Roles
- **Pet Owner:** Lists pets for adoption.
- **Adopter:** Seeks pets for adoption.

### Key Features
- **Pet Owner:**
  - Account creation and management.
  - Pet listing and updates.
- **Adopter:**
  - Account creation and management.
  - Browse and receive pet notifications.

### Resource Paths
- **Microservice 1: Pets Service**
  - Query available pet lists.
  - Create and update pet listings.
- **Microservice 2: Adopter Profile Service**
  - Get and update adopter information.
- **Microservice 3: Pet Owner Service**
  - Create, update, and delete pet owner profiles.
- **API Gateway** for routing requests.
  
### Architecture
- **AWS S3** for static web assets.
- **AWS API Gateway** as a single entry point.
- **AWS Cognito** for authentication.
- **AWS Elastic Beanstalk** for service deployment.
- **EC2, Docker, RDS** for microservices.
- **PetFinder API via Lambda** for web scraping.
- **AWS SNS** for notifications.
- **CI/CD pipeline** for continuous deployment.
![image](https://github.com/LuminaScript/AWS-Pet-Adopt-Web/assets/98562104/931400a5-51ad-4de0-9e4d-cd5b85ce7cbd)

### Deployment Links
- **Front-end:** [Static Website](http://6156-frontend.s3-website-us-east-1.amazonaws.com)
- **Microservice 1:** [Elastic Beanstalk](http://6156beanstalk-env.eba-r5bpgvxm.us-east-1.elasticbeanstalk.com:8012/)
- **Microservice 2:** [Docker on EC2](http://ec2-52-90-97-138.compute-1.amazonaws.com/)
- **Microservice 3:** [EC2](http://ec2-52-90-97-138.compute-1.amazonaws.com/)

### Additional Resources
- [Swagger File](https://gist.github.com/LuminaScript/751061e5d2eb152bf87d0437e820fba1)
