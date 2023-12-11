const acordeonTrigger = document.querySelectorAll('.acordeon .trigger')

acordeonTrigger.forEach((trigger) => {
    trigger.addEventListener('click', () => {
        trigger.parentNode.classList.toggle('open')
    })
})