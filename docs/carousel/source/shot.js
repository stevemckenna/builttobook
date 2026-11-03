const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const out=process.argv[2];
for(const n of JSON.parse(fs.readFileSync('list.json'))){for(const [m,h] of [['post',1350],['reel',1920]]){
const p=await b.newPage({viewport:{width:1080,height:h}});await p.goto('file://'+process.cwd()+`/${n}-${m}.html`);
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:`${out}/${m}/${n}.png`,clip:{x:0,y:0,width:1080,height:h}});await p.close();}}
await b.close();})();
