import * as bindings from 'bindings';

const addon = bindings('addon');

const result:number = addon.add(1, 2);

console.log('result: ', result);