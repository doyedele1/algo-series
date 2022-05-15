"use strict";

function inventoryList() {
	let items = [
        { name: 'Segun' },
        { name: 'Kayode' },
        { name: 'Deborah' }
	];

	const add = (name) => {
        const names = items.filter(item => item.name === name);
        if (names.length === 0) {
            items.push({name: name});
        }
	}

	const remove = (name) => {
        items = items.filter(item => item.name !== name);
	}

	const getList = () => {
        return items;
	}

    getList();
    add('Segun');
    getList();
    add('Kayode');
    getList();
    remove('Segun');
    getList();
    add('Deborah');
    getList();
    add('Segun');
    getList();

	return {add, remove, getList};
}

inventoryList();