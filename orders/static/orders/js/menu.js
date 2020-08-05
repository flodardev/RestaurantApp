document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#next').onclick = () => {
        let el = document.querySelector('#next')
        let name = el.closest('#pizza_name').value;
        console.log(name)
        document.querySelector('#toppingModalLongTitle').innerHTML = name;
    }
});