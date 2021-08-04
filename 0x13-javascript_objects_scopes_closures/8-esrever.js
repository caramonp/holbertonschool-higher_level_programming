#!/usr/bin/node
exports.esrever = function (list) {
  const NewArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    NewArray.push(list[i]);
  }
  return (NewArray);
};
