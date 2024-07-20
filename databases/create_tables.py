import boto3

def create_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    User = {
        'TableName': 'User',
        'KeySchema': [
            {'AttributeName': 'NetID', 'KeyType': 'HASH'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'UserID', 'AttributeType': 'N'}
            
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    }

    table = dynamodb.create_table(**courses)
    table.wait_until_exists()
    print("Courses table created successfully!")


    
    schedule = {
        'TableName': 'Schedule',
        'KeySchema': [
            {'AttributeName': 'ScheduleID', 'KeyType': 'HASH'},
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'ScheduleID', 'AttributeType': 'N'},
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    }

    table = dynamodb.create_table(**schedule)
    table.wait_until_exists()
    print("Schedule table created successfully!")
    
    
    courses = {
        'TableName': 'Courses',
        'KeySchema': [
            {'AttributeName': 'CourseID', 'KeyType': 'HASH'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'CourseID', 'AttributeType': 'N'}
            
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    }

    table = dynamodb.create_table(**courses)
    table.wait_until_exists()
    print("Courses table created successfully!")


if __name__ == '__main__':
    create_table()
