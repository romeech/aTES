# SERVICES
1. auth
2. task tracker
3. billing
4. analytics
5. notifications

Consumers are specified in brackets to each event.

## Auth
### Biz events
* User Logged In
* User Created
* User Role Changed

### CUD events
#### Users
* Task Tracker (user ID, role)
* Billing (user ID, role, name, email)
* Analytics (user ID, name, role)
* Notifications (user ID, email)

## Task Tracker

### Biz events
* Task Created (Notifications)
* Task Assigned (Billing)
* Task Closed (Billing)

### CUD events
#### Tasks
* Billing (task ID, assignee ID, title, description, fee, amount, status, created_at)
* Analytics (task ID, assignee ID, title, fee, amount, status, created_at)
* Notifications (task ID, assignee ID, title, description)

## Billing

### Biz events
* User Account Created (Analytics)
* User Account Decreased
* User Account Increased
* Negative Balance (Analytics)
* Positive Balance (Analytics)
* User Got Income (Notifications)

### CUD events
#### Balance (Analytics)
#### Audit Log (Analytics)

