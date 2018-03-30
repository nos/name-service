# nOS Name Service Smart Contract

---

# 1. Nameservice

## MVP Features

* Admin can register domain names on behalf of other users.

* Admin can delete domains.

* Domain owners can change the target URL (Github Pages).

## Examples

### 1. RegisterDomain

Register a new domain, set a target URL, and optionally give ownership to different account.

For the MVP, only the hardcoded admin (`owner`) can invoke `RegisterDomain`

```
'RegisterDomain' ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y', 'somedomain.nos', 'https://deanpress.github.com/some-site-repo', 'AMrLse3suPd123HjSanwefCC5WQZPmjDYv']
```

* `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y` is the address of the invoking user. Before executing the operation, `CheckWitness()` is run on this argument, to make sure that the invoker is who they say they are. In this case, because we're registering a domain (Admin exclusive operation): it should always be `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`, the hardcoded admin domain.

* `somedomain.nos` is the domain we wish to register.

* `https://deanpress.github.com/some-site-repo` is the URL we wish to point it to.

* `AMrLse3suPd123HjSanwefCC5WQZPmjDYv` is the "registrant". The address of the account we want to give the domain's priveledges to. Next to the hardcoded Admin account, this account will be able to invoke `SetDomainTarget`.


### 2. SetDomainTarget

Set the target domain.

For the MVP, both the hardcoded admin and the registrant can invoke `SetDomainTarget`.


```
'SetDomainTarget' ['AMrLse3suPd123HjSanwefCC5WQZPmjDYv', 'somedomain.nos', 'https://different-url.github.com/different-site']
```

* `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y` is the address of the invoking user.

* `somedomain.nos` is the domain we wish to register. We have to be the registrar or the hardcoded admin account.

### 3. DeleteDomain

Delete a domain.

For the MVP, only the hardcoded admin can invoke `DeleteDomain`.

```
'DeleteDomain' ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y', 'somedomain.nos']
```

## Nameservice Client <> Contract Resolver Flow

![Domain Resolver Flow](https://i.imgur.com/P9oyyAH.jpg)
