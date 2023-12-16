function show(ans) {
    a = document.getElementById(ans);
//    b = document.getElementById(btn);
    if (a.style.display === 'none') {
        a.style.display='block';
    } else {
        a.style.display='none';
    }
};

const pick = () => {
    a = document.getElementById('star');
    c = document.getElementById('check');
    f = document.getElementById('memorizeForm');
    if (a.style.color === 'black'){
       a.style.color = 'gold';
       c.checked = true;
    } else {
        a.style.color = 'black';
        c.checked = false;
    }
}