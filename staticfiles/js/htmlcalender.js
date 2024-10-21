document.addEventListener('DOMContentLoaded', (event) => {

    const tables = document.getElementsByTagName('table')
    Array.from(tables).forEach(table => {
        table.classList.add('min-w-full', 'table-auto', 'border-collapse', 'border', 'border-gray-200')
    })

    const tds = document.getElementsByTagName('td')

    Array.from(tds).forEach(td => {
        td.classList.add('pl-16', 'text-lg', 'text-gray-700', 'border', 'border-gray-200')

    })

    const ths = document.getElementsByTagName('th')
    Array.from(ths).forEach(th => {
        th.classList.add('mb-4', 'text-red-500')

    })


})