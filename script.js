document.getElementById('userForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const dob = document.getElementById('dob').value;

    await fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, dob })
    });

    loadUsers();
});

async function loadUsers() {
    const res = await fetch('http://localhost:5000/users');
    const users = await res.json();
    const list = document.getElementById('userList');
    list.innerHTML = '';
    users.forEach(user => {
        const item = document.createElement('li');
        item.textContent = `${user[0]} - ${user[1]} (${user[2]})`;
        list.appendChild(item);
    });
}

loadUsers();
