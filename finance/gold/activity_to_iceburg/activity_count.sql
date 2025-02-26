select contact.*
from 
crm.contact contact
left join crm.account account on contact.account_id = account.id 
where account.id is not null 