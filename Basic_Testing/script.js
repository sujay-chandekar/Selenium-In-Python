const alert1 = ()=>{
    alert('Alert from script.js');
}

const alert2 = ()=>{
    setTimeout(function() {
        alert("This alert appeared after a 3-second delay!");
    },4000); // 4000 milliseconds
}

/* DOM behaviors for Selenium practice */
document.addEventListener('DOMContentLoaded', ()=>{
    // Form submit -> show greeting
    const form = document.getElementById('practiceForm');
    const nameInput = document.getElementById('nameInput');
    const greeting = document.getElementById('greeting');

    if(form){
        form.addEventListener('submit', (e)=>{
            e.preventDefault();
            const name = nameInput.value.trim() || 'Guest';
            greeting.textContent = `Hello, ${name}! (submitted)`;
        });
    }

    // Delayed content
    const showDelayedBtn = document.getElementById('showDelayedBtn');
    const delayedContent = document.getElementById('delayedContent');
    if(showDelayedBtn && delayedContent){
        showDelayedBtn.addEventListener('click', (e)=>{
            e.preventDefault();
            // hide first
            delayedContent.hidden = true;
            setTimeout(()=>{
                delayedContent.hidden = false;
            }, 3000);
        });
    }

    // Modal open/close
    const openModalBtn = document.getElementById('openModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const modal = document.getElementById('practiceModal');
    if(openModalBtn && modal){
        openModalBtn.addEventListener('click', (e)=>{
            e.preventDefault();
            modal.hidden = false;
            modal.setAttribute('aria-hidden','false');
            // move focus into modal
            closeModalBtn && closeModalBtn.focus();
        });
    }
    if(closeModalBtn && modal){
        closeModalBtn.addEventListener('click', ()=>{
            modal.hidden = true;
            modal.setAttribute('aria-hidden','true');
            openModalBtn && openModalBtn.focus();
        });
    }

    // Add row to local table
    const addRowBtn = document.getElementById('addRowBtn');
    const tableBody = document.querySelector('#practiceTable tbody');
    let rowCount = 0;
    if(addRowBtn && tableBody){
        addRowBtn.addEventListener('click', (e)=>{
            e.preventDefault();
            rowCount += 1;
            const tr = document.createElement('tr');
            const td1 = document.createElement('td');
            td1.textContent = rowCount;
            const td2 = document.createElement('td');
            td2.textContent = nameInput.value.trim() || `Row ${rowCount}`;
            const td3 = document.createElement('td');
            const del = document.createElement('button');
            del.textContent = 'Delete';
            del.addEventListener('click', ()=> tr.remove());
            td3.appendChild(del);
            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);
            tableBody.appendChild(tr);
        });
    }
});