const fs = require('fs');

const alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const numbers = contents.split(' ').map(s => parseInt(s));
    let index = 0;

    const node = createNode()
    const sum = sumMetaInfo(node);
    console.log(sum);

    const coolSum = complexSum(node);
    console.log(coolSum);

    function createNode() {
        const childNodesCount = numbers[index];
        index++;
        const metaInfoCount = numbers[index];
        index++;
        const children = [];

        for (let i = 0; i < childNodesCount; i++) {
            children.push(createNode(index))
        }

        const metaInfo = [];
        for (let i = 0; i < metaInfoCount; i++) {
            metaInfo.push(numbers[index]);
            index++;
        }

        return {
            children,
            metaInfo
        }
    }

    function sumMetaInfo(node) {
        return node.metaInfo.reduce((acc, meta) => acc + meta, 0) + node.children.reduce((acc, c) => acc + sumMetaInfo(c), 0);
    }

    function complexSum(node) {
        if (node.children.length === 0) {
            return sumMetaInfo(node);
        } else {
            return node.metaInfo.reduce((acc, meta) => {
                if (meta < 1) {
                    return acc;
                }

                const someChild = node.children[meta - 1];
                if (someChild) {
                    return complexSum(someChild) + acc;
                }

                return acc;
            }, 0)
        }
    }
})