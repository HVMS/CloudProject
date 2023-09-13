# _Just Click - Online Order System based on Cloud_

- "Just Click" is a SAAS model system in which a user is supposed to upload an image of handwritten notes of vegetable items vs. quantity. After that using
  Amazon's Machine Learning-based service,   we will extract important information and check against the vegetable items database with the quantity. If all
  the items are matched, the full order email will be sent otherwise a partial order will be delivered. I have focused here mostly on the backend part to use
  different types of cloud services based on storage, network, serverless functions, computing, and other services.

# Backend Architecture 

![image](https://github.com/HVMS/CloudProect/assets/38061955/eafbb9eb-de7d-4b47-bbfb-f9a285405478)

# Amazon Services Used

- Compute Services
  - AWS Lambda 
  - AWS Step Function

- Network Services
  - Amazon API Gateway ( RESTFul Architecture APIs )
 
- Serverless Services
  - AWS Lambda ( To execute shorter computation with less time )
  - AWS Step Function ( To execute workflow seamlessly and faster execution )
 
- Other Services
  - Amazon SNS (To Send an email to a group of users)
  - Amazon Textract ( TO extract image data - own algorithm implemented )
 
 

