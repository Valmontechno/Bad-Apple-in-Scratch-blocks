p = JSON.parse(document.body.innerText);
p.targets[1].blocks = {}
width = 28;
height = 20;
for (i=0; i<width; i++){
    for (j=0; j<height; j++) {
        n = i + j*width + 1
        block = {
          "opcode": "event_whenbroadcastreceived",
          "next": 'b'+n,
          "parent": null,
          "inputs": {},
          "fields": { "BROADCAST_OPTION": [n, 'f'+n] },
          "shadow": false,
          "topLevel": true,
          "x": i*113,
          "y": j*108
        }
        p.targets[1].blocks['a'+n] = block;
        block = {
          "opcode": "procedures_call",
          "next": null,
          "parent": 'a'+n,
          "inputs": { "jW8UEuDud8%BwdH}Y!b^": [1, [10, String(n).padStart(3,'0')]] },
          "fields": {},
          "shadow": false,
          "topLevel": false,
          "mutation": {
            "tagName": "mutation",
            "children": [],
            "proccode": "%s",
            "argumentids": "[\"jW8UEuDud8%BwdH}Y!b^\"]",
            "warp": "false"
          }
        }
        p.targets[1].blocks['b'+n] = block;
    }
}
d = JSON.stringify(p)