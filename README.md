# Event_Registration
This project provides a simple event registration platform where users can register for an event by submitting their details through a web form. The data is stored in Amazon DynamoDB, and users receive an email confirmation via Amazon SES. The frontend communicates with the backend through Amazon API Gateway, which integrates with AWS Lambda.

# AWS Services Used
## Amazon S3 (Frontend Hosting)
Stores and serves the HTML, CSS, and JavaScript files for the registration form.
Provides a static website endpoint for frontend hosting.

## Amazon API Gateway
Exposes a REST API endpoint for the frontend to communicate with the backend.
Handles CORS configuration to allow browser requests.
Routes incoming requests to the AWS Lambda function.

## AWS Lambda
Backend logic to process event registration.
Extracts registration details from API Gateway requests.
Stores data in DynamoDB.
Sends email notification via Amazon SES.

## Amazon DynamoDB
A fully managed NoSQL database used to store event registration details.
Table structure:
Partition Key: eventid
Attributes: eventname, cname, cemail

## Amazon SES (Simple Email Service)
Sends confirmation emails to the user after successful registration.
Configured with verified email/domain.

# System Architecture Flow

## User Interaction
The user opens the registration page hosted on S3 (or local via Live Server during dev).
Fills in the form: cname, cemail, eventid, eventname.
API Request
JavaScript code submits form data using Fetch API as a JSON POST request.

## API Gateway
Receives request.
Validates method and CORS headers.
Passes payload to the Lambda function.

## Lambda Execution
Parses request body.
Inserts record into DynamoDB:
Sends confirmation email using SES.
Returns JSON response with success message.

## Frontend Response
Displays confirmation message (e.g., "Registration successful!").
User receives an email notification.

# Frontend (HTML + CSS + JavaScript)
HTML Form: Collects user details.
CSS File: Provides styling (header, centered form, responsive design).
JavaScript: Submits data via Fetch API to API Gateway.

## LAmbda function python

## Database (DynamoDB Table Design)
Table Name: eventmanagement
Primary Key: eventid (String)
Attributes:
eventname (String)
cname (String)
cemail (String)

# Email (SES Configuration)

Verify sender domain or email in SES.
Configure region (SES sandbox requires verification for both sender & receiver emails).
Grant Lambda execution role SES send permission.

# IAM Roles & Permissions
Lambda Execution Role should have:
dynamodb:PutItem for eventmanagement table.
ses:SendEmail permission.
Basic Lambda logging policy (AWSLambdaBasicExecutionRole).
