import boto3
from botocore.exceptions import ClientError

def conditional_put():
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName='Courses',
            Item={
                "CourseID": {
                    'S': '2942'
                },
                'Subject_Area': {
                    'S': 'CSE'
                },
                'Course_Number':{
                    'N': '2102' #number passed in as a string (ie in quotes)
                },
                'Instructor':{
                    'S': "Jonathan Clark"
                },
                'Course_Name':{
                    'S': "Introduction to Software Engineering"
                },
                'Description':{
                    'S': "Software engineering concepts including the software life cycle and other software-development process models. Specification techniques, design methodologies, performance analysis, and verification techniques. Team-oriented software design and development, and project management techniques.Use of appropriate design and debugging tools for a modern programming language. Homework and laboratory projects that emphasize design and the use/features of a modern programming language."
                }
            },
            ConditionExpression='attribute_not_exists(product_name)'
        )
    except ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise

if __name__ == '__main__':
    conditional_put()
    print('Done')

