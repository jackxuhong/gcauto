# gcauto

Google Classroom Automation

## Dependencies

```
pip install flask python-dotenv authlib google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## High-level Design

### Features

- User selects a Google Classroom (course) to be managed by GCA
- User creates a template for recurring assignments
- User adds a recurring assignment to a managed classroom
- GCA creates an assignment as per User's template
