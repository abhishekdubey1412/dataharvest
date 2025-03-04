# html = """
        
# 	<!DOCTYPE html>
# <html lang="en">
# <head>

	
# 		<meta charset="utf-8"><script type="text/javascript">(window.NREUM||(NREUM={})).init={privacy:{cookies_enabled:true},ajax:{deny_list:["bam.nr-data.net"]},distributed_tracing:{enabled:true}};(window.NREUM||(NREUM={})).loader_config={agentID:"1386014001",accountID:"3701079",trustKey:"66686",xpid:"VwEHUFZUARABV1FQBAEGU1UE",licenseKey:"NRJS-2c42fcd46722616451c",applicationID:"1302301515"};;/*! For license information please see nr-loader-spa-1.283.2.min.js.LICENSE.txt */
# (()=>{var e,t,r={8122:(e,t,r)=>{"use strict";r.d(t,{a:()=>i});var n=r(944);function i(e,t){try{if(!e||"object"!=typeof e)return(0,n.R)(3);if(!t||"object"!=typeof t)return(0,n.R)(4);const r=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),o=0===Object.keys(r).length?e:r;for(let a in o)if(void 0!==e[a])try{if(null===e[a]){r[a]=null;continue}Array.isArray(e[a])&&Array.isArray(t[a])?r[a]=Array.from(new Set([...e[a],...t[a]])):"object"==typeof e[a]&&"object"==typeof t[a]?r[a]=i(e[a],t[a]):r[a]=e[a]}catch(e){(0,n.R)(1,e)}return r}catch(e){(0,n.R)(2,e)}}},2555:(e,t,r)=>{"use strict";r.d(t,{Vp:()=>c,fn:()=>s,x1:()=>u});var n=r(384),i=r(8122);const o={beacon:n.NT.beacon,errorBeacon:n.NT.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0},a={};function s(e){try{const t=c(e);return!!t.licenseKey&&!!t.errorBeacon&&!!t.applicationID}catch(e){return!1}}function c(e){if(!e)throw new Error("All info objects require an agent identifier!");if(!a[e])throw new Error("Info for ".concat(e," was never set"));return a[e]}function u(e,t){if(!e)throw new Error("All info objects require an agent identifier!");a[e]=(0,i.a)(t,o);const r=(0,n.nY)(e);r&&(r.info=a[e])}},9417:(e,t,r)=>{"use strict";r.d(t,{D0:()=>h,gD:()=>g,xN:()=>p});var n=r(3333);const i=e=>{if(!e||"string"!=typeof e)return!1;try{document.createDocumentFragment().querySelector(e)}catch{return!1}return!0};var o=r(2614),a=r(944),s=r(384),c=r(8122);const u="[data-nr-mask]",d=()=>{const e={feature_flags:[],experimental:{marks:!1,measures:!1,resources:!1},mask_selector:"*",block_selector:"[data-nr-block]",mask_input_options:{color:!1,date:!1,"datetime-local":!1,email:!1,month:!1,number:!1,range:!1,search:!1,tel:!1,text:!1,time:!1,url:!1,week:!1,textarea:!1,select:!1,password:!0}};return{ajax:{deny_list:void 0,block_internal:!0,enabled:!0,autoStart:!0},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},get feature_flags(){return e.feature_flags},set feature_flags(t){e.feature_flags=t},generic_events:{enabled:!0,autoStart:!0},harvest:{interval:30},jserrors:{enabled:!0,autoStart:!0},logging:{enabled:!0,autoStart:!0},metrics:{enabled:!0,autoStart:!0},obfuscate:void 0,page_action:{enabled:!0},page_view_event:{enabled:!0,autoStart:!0},page_view_timing:{enabled:!0,autoStart:!0},performance:{get capture_marks(){return e.feature_flags.includes(n.$v.MARKS)||e.experimental.marks},set capture_marks(t){e.experimental.marks=t},get capture_measures(){return e.feature_flags.includes(n.$v.MEASURES)||e.experimental.measures},set capture_measures(t){e.experimental.measures=t},capture_detail:!0,resources:{get enabled(){return e.feature_flags.includes(n.$v.RESOURCES)||e.experimental.resources},set enabled(t){e.experimental.resources=t},asset_types:[],first_party_domains:[],ignore_newrelic:!0}},privacy:{cookies_enabled:!0},proxy:{assets:void 0,beacon:void 0},session:{expiresMs:o.wk,inactiveMs:o.BB},session_replay:{autoStart:!0,enabled:!1,preload:!1,sampling_rate:10,error_sampling_rate:100,collect_fonts:!1,inline_images:!1,fix_stylesheets:!0,mask_all_inputs:!0,get mask_text_selector(){return e.mask_selector},set mask_text_selector(t){i(t)?e.mask_selector="".concat(t,",").concat(u):""===t||null===t?e.mask_selector=u:(0,a.R)(5,t)},get block_class(){return"nr-block"},get ignore_class(){return"nr-ignore"},get mask_text_class(){return"nr-mask"},get block_selector(){return e.block_selector},set block_selector(t){i(t)?e.block_selector+=",".concat(t):""!==t&&(0,a.R)(6,t)},get mask_input_options(){return e.mask_input_options},set mask_input_options(t){t&&"object"==typeof t?e.mask_input_options={...t,password:!0}:(0,a.R)(7,t)}},session_trace:{enabled:!0,autoStart:!0},soft_navigations:{enabled:!0,autoStart:!0},spa:{enabled:!0,autoStart:!0},ssl:void 0,user_actions:{enabled:!0,elementAttributes:["id","className","tagName","type"]}}},l={},f="All configuration objects require an agent identifier!";function h(e){if(!e)throw new Error(f);if(!l[e])throw new Error("Configuration for ".concat(e," was never set"));return l[e]}function p(e,t){if(!e)throw new Error(f);l[e]=(0,c.a)(t,d());const r=(0,s.nY)(e);r&&(r.init=l[e])}function g(e,t){if(!e)throw new Error(f);var r=h(e);if(r){for(var n=t.split("."),i=0;i<n.length-1;i++)if("object"!=typeof(r=r[n[i]]))return;r=r[n[n.length-1]]}return r}},5603:(e,t,r)=>{"use strict";r.d(t,{a:()=>c,o:()=>s});var n=r(384),i=r(8122);const o={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},a={};function s(e){if(!e)throw new Error("All loader-config objects require an agent identifier!");if(!a[e])throw new Error("LoaderConfig for ".concat(e," was never set"));return a[e]}function c(e,t){if(!e)throw new Error("All loader-config objects require an agent identifier!");a[e]=(0,i.a)(t,o);const r=(0,n.nY)(e);r&&(r.loader_config=a[e])}},3371:(e,t,r)=>{"use strict";r.d(t,{V:()=>f,f:()=>l});var n=r(8122),i=r(384),o=r(6154),a=r(9324);let s=0;const c={buildEnv:a.F3,distMethod:a.Xs,version:a.xv,originTime:o.WN},u={customTransaction:void 0,disabled:!1,isolatedBacklog:!1,loaderType:void 0,maxBytes:3e4,onerror:void 0,ptid:void 0,releaseIds:{},appMetadata:{},session:void 0,denyList:void 0,timeKeeper:void 0,obfuscator:void 0,harvester:void 0},d={};function l(e){if(!e)throw new Error("All runtime objects require an agent identifier!");if(!d[e])throw new Error("Runtime for ".concat(e," was never set"));return d[e]}function f(e,t){if(!e)throw new Error("All runtime objects require an agent identifier!");d[e]={...(0,n.a)(t,u),...c},Object.hasOwnProperty.call(d[e],"harvestCount")||Object.defineProperty(d[e],"harvestCount",{get:()=>++s});const r=(0,i.nY)(e);r&&(r.runtime=d[e])}},9324:(e,t,r)=>{"use strict";r.d(t,{F3:()=>i,Xs:()=>o,Yq:()=>a,xv:()=>n});const n="1.283.2",i="PROD",o="CDN",a="^2.0.0-alpha.17"},6154:(e,t,r)=>{"use strict";r.d(t,{A4:()=>s,OF:()=>d,RI:()=>i,WN:()=>h,bv:()=>o,gm:()=>a,lR:()=>f,m:()=>u,mw:()=>c,sb:()=>l});var n=r(1863);const i="undefined"!=typeof window&&!!window.document,o="undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis.navigator instanceof WorkerNavigator),a=i?window:"undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis),s="complete"===a?.document?.readyState,c=Boolean("hidden"===a?.document?.visibilityState),u=""+a?.location,d=/iPad|iPhone|iPod/.test(a.navigator?.userAgent),l=d&&"undefined"==typeof SharedWorker,f=(()=>{const e=a.navigator?.userAgent?.match(/Firefox[/\s](\d+\.\d+)/);return Array.isArray(e)&&e.length>=2?+e[1]:0})(),h=Date.now()-(0,n.t)()},7295:(e,t,r)=>{"use strict";r.d(t,{Xv:()=>a,gX:()=>i,iW:()=>o});var n=[];function i(e){if(!e||o(e))return!1;if(0===n.length)return!0;for(var t=0;t<n.length;t++){var r=n[t];if("*"===r.hostname)return!1;if(s(r.hostname,e.hostname)&&c(r.pathname,e.pathname))return!1}return!0}function o(e){return void 0===e.hostname}function a(e){if(n=[],e&&e.length)for(var t=0;t<e.length;t++){let r=e[t];if(!r)continue;0===r.indexOf("http://")?r=r.substring(7):0===r.indexOf("https://")&&(r=r.substring(8));const i=r.indexOf("/");let o,a;i>0?(o=r.substring(0,i),a=r.substring(i)):(o=r,a="");let[s]=o.split(":");n.push({hostname:s,pathname:a})}}function s(e,t){return!(e.length>t.length)&&t.indexOf(e)===t.length-e.length}function c(e,t){return 0===e.indexOf("/")&&(e=e.substring(1)),0===t.indexOf("/")&&(t=t.substring(1)),""===e||e===t}},1687:(e,t,r)=>{"use strict";r.d(t,{Ak:()=>c,Ze:()=>l,x3:()=>u});var n=r(7836),i=r(3606),o=r(860),a=r(2646);const s={};function c(e,t){const r={staged:!1,priority:o.P3[t]||0};d(e),s[e].get(t)||s[e].set(t,r)}function u(e,t){e&&s[e]&&(s[e].get(t)&&s[e].delete(t),h(e,t,!1),s[e].size&&f(e))}function d(e){if(!e)throw new Error("agentIdentifier required");s[e]||(s[e]=new Map)}function l(e="",t="feature",r=!1){if(d(e),!e||!s[e].get(t)||r)return h(e,t);s[e].get(t).staged=!0,f(e)}function f(e){const t=Array.from(s[e]);t.every((([e,t])=>t.staged))&&(t.sort(((e,t)=>e[1].priority-t[1].priority)),t.forEach((([t])=>{s[e].delete(t),h(e,t)})))}function h(e,t,r=!0){const o=e?n.ee.get(e):n.ee,s=i.i.handlers;if(!o.aborted&&o.backlog&&s){if(r){const e=o.backlog[t],r=s[t];if(r){for(let t=0;e&&t<e.length;++t)p(e[t],r);Object.entries(r).forEach((([e,t])=>{Object.values(t||{}).forEach((t=>{t[0]?.on&&t[0]?.context()instanceof a.y&&t[0].on(e,t[1])}))}))}}o.isolatedBacklog||delete s[t],o.backlog[t]=null,o.emit("drain-"+t,[])}}function p(e,t){var r=e[1];Object.values(t[r]||{}).forEach((t=>{var r=e[0];if(t[0]===r){var n=t[1],i=e[3],o=e[2];n.apply(i,o)}}))}},7836:(e,t,r)=>{"use strict";r.d(t,{P:()=>c,ee:()=>u});var n=r(384),i=r(8990),o=r(3371),a=r(2646),s=r(5607);const c="nr@context:".concat(s.W),u=function e(t,r){var n={},s={},d={},l=!1;try{l=16===r.length&&(0,o.f)(r).isolatedBacklog}catch(e){}var f={on:p,addEventListener:p,removeEventListener:function(e,t){var r=n[e];if(!r)return;for(var i=0;i<r.length;i++)r[i]===t&&r.splice(i,1)},emit:function(e,r,n,i,o){!1!==o&&(o=!0);if(u.aborted&&!i)return;t&&o&&t.emit(e,r,n);for(var a=h(n),c=g(e),d=c.length,l=0;l<d;l++)c[l].apply(a,r);var p=v()[s[e]];p&&p.push([f,e,r,a]);return a},get:m,listeners:g,context:h,buffer:function(e,t){const r=v();if(t=t||"feature",f.aborted)return;Object.entries(e||{}).forEach((([e,n])=>{s[n]=t,t in r||(r[t]=[])}))},abort:function(){f._aborted=!0,Object.keys(f.backlog).forEach((e=>{delete f.backlog[e]}))},isBuffering:function(e){return!!v()[s[e]]},debugId:r,backlog:l?{}:t&&"object"==typeof t.backlog?t.backlog:{},isolatedBacklog:l};return Object.defineProperty(f,"aborted",{get:()=>{let e=f._aborted||!1;return e||(t&&(e=t.aborted),e)}}),f;function h(e){return e&&e instanceof a.y?e:e?(0,i.I)(e,c,(()=>new a.y(c))):new a.y(c)}function p(e,t){n[e]=g(e).concat(t)}function g(e){return n[e]||[]}function m(t){return d[t]=d[t]||e(f,t)}function v(){return f.backlog}}(void 0,"globalEE"),d=(0,n.Zm)();d.ee||(d.ee=u)},2646:(e,t,r)=>{"use strict";r.d(t,{y:()=>n});class n{constructor(e){this.contextId=e}}},9908:(e,t,r)=>{"use strict";r.d(t,{d:()=>n,p:()=>i});var n=r(7836).ee.get("handle");function i(e,t,r,i,o){o?(o.buffer([e],i),o.emit(e,t,r)):(n.buffer([e],i),n.emit(e,t,r))}},3606:(e,t,r)=>{"use strict";r.d(t,{i:()=>o});var n=r(9908);o.on=a;var i=o.handlers={};function o(e,t,r,o){a(o||n.d,i,e,t,r)}function a(e,t,r,i,o){o||(o="feature"),e||(e=n.d);var a=t[o]=t[o]||{};(a[r]=a[r]||[]).push([e,i])}},3878:(e,t,r)=>{"use strict";function n(e,t){return{capture:e,passive:!1,signal:t}}function i(e,t,r=!1,i){window.addEventListener(e,t,n(r,i))}function o(e,t,r=!1,i){document.addEventListener(e,t,n(r,i))}r.d(t,{DD:()=>o,jT:()=>n,sp:()=>i})},5607:(e,t,r)=>{"use strict";r.d(t,{W:()=>n});const n=(0,r(9566).bz)()},9566:(e,t,r)=>{"use strict";r.d(t,{LA:()=>s,ZF:()=>c,bz:()=>a,el:()=>u});var n=r(6154);const i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";function o(e,t){return e?15&e[t]:16*Math.random()|0}function a(){const e=n.gm?.crypto||n.gm?.msCrypto;let t,r=0;return e&&e.getRandomValues&&(t=e.getRandomValues(new Uint8Array(30))),i.split("").map((e=>"x"===e?o(t,r++).toString(16):"y"===e?(3&o()|8).toString(16):e)).join("")}function s(e){const t=n.gm?.crypto||n.gm?.msCrypto;let r,i=0;t&&t.getRandomValues&&(r=t.getRandomValues(new Uint8Array(e)));const a=[];for(var s=0;s<e;s++)a.push(o(r,i++).toString(16));return a.join("")}function c(){return s(16)}function u(){return s(32)}},2614:(e,t,r)=>{"use strict";r.d(t,{BB:()=>a,H3:()=>n,g:()=>u,iL:()=>c,tS:()=>s,uh:()=>i,wk:()=>o});const n="NRBA",i="SESSION",o=144e5,a=18e5,s={STARTED:"session-started",PAUSE:"session-pause",RESET:"session-reset",RESUME:"session-resume",UPDATE:"session-update"},c={SAME_TAB:"same-tab",CROSS_TAB:"cross-tab"},u={OFF:0,FULL:1,ERROR:2}},1863:(e,t,r)=>{"use strict";function n(){return Math.floor(performance.now())}r.d(t,{t:()=>n})},7485:(e,t,r)=>{"use strict";r.d(t,{D:()=>i});var n=r(6154);function i(e){if(0===(e||"").indexOf("data:"))return{protocol:"data"};try{const t=new URL(e,location.href),r={port:t.port,hostname:t.hostname,pathname:t.pathname,search:t.search,protocol:t.protocol.slice(0,t.protocol.indexOf(":")),sameOrigin:t.protocol===n.gm?.location?.protocol&&t.host===n.gm?.location?.host};return r.port&&""!==r.port||("http:"===t.protocol&&(r.port="80"),"https:"===t.protocol&&(r.port="443")),r.pathname&&""!==r.pathname?r.pathname.startsWith("/")||(r.pathname="/".concat(r.pathname)):r.pathname="/",r}catch(e){return{}}}},944:(e,t,r)=>{"use strict";function n(e,t){"function"==typeof console.debug&&console.debug("New Relic Warning: https://github.com/newrelic/newrelic-browser-agent/blob/main/docs/warning-codes.md#".concat(e),t)}r.d(t,{R:()=>n})},5284:(e,t,r)=>{"use strict";r.d(t,{t:()=>c,B:()=>s});var n=r(7836),i=r(6154);const o="newrelic";const a=new Set,s={};function c(e,t){const r=n.ee.get(t);s[t]??={},e&&"object"==typeof e&&(a.has(t)||(r.emit("rumresp",[e]),s[t]=e,a.add(t),function(e={}){try{i.gm.dispatchEvent(new CustomEvent(o,{detail:e}))}catch(e){}}({loaded:!0})))}},8990:(e,t,r)=>{"use strict";r.d(t,{I:()=>i});var n=Object.prototype.hasOwnProperty;function i(e,t,r){if(n.call(e,t))return e[t];var i=r();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},6389:(e,t,r)=>{"use strict";function n(e,t=500,r={}){const n=r?.leading||!1;let i;return(...r)=>{n&&void 0===i&&(e.apply(this,r),i=setTimeout((()=>{i=clearTimeout(i)}),t)),n||(clearTimeout(i),i=setTimeout((()=>{e.apply(this,r)}),t))}}function i(e){let t=!1;return(...r)=>{t||(t=!0,e.apply(this,r))}}r.d(t,{J:()=>i,s:()=>n})},3304:(e,t,r)=>{"use strict";r.d(t,{A:()=>o});var n=r(7836);const i=()=>{const e=new WeakSet;return(t,r)=>{if("object"==typeof r&&null!==r){if(e.has(r))return;e.add(r)}return r}};function o(e){try{return JSON.stringify(e,i())??""}catch(e){try{n.ee.emit("internal-error",[e])}catch(e){}return""}}},5289:(e,t,r)=>{"use strict";r.d(t,{GG:()=>o,sB:()=>a});var n=r(3878);function i(){return"undefined"==typeof document||"complete"===document.readyState}function o(e,t){if(i())return e();(0,n.sp)("load",e,t)}function a(e){if(i())return e();(0,n.DD)("DOMContentLoaded",e)}},384:(e,t,r)=>{"use strict";r.d(t,{NT:()=>o,US:()=>d,Zm:()=>a,bQ:()=>c,dV:()=>s,nY:()=>u,pV:()=>l});var n=r(6154),i=r(1863);const o={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function a(){return n.gm.NREUM||(n.gm.NREUM={}),void 0===n.gm.newrelic&&(n.gm.newrelic=n.gm.NREUM),n.gm.NREUM}function s(){let e=a();return e.o||(e.o={ST:n.gm.setTimeout,SI:n.gm.setImmediate,CT:n.gm.clearTimeout,XHR:n.gm.XMLHttpRequest,REQ:n.gm.Request,EV:n.gm.Event,PR:n.gm.Promise,MO:n.gm.MutationObserver,FETCH:n.gm.fetch,WS:n.gm.WebSocket}),e}function c(e,t){let r=a();r.initializedAgents??={},t.initializedAt={ms:(0,i.t)(),date:new Date},r.initializedAgents[e]=t}function u(e){let t=a();return t.initializedAgents?.[e]}function d(e,t){a()[e]=t}function l(){return function(){let e=a();const t=e.info||{};e.info={beacon:o.beacon,errorBeacon:o.errorBeacon,...t}}(),function(){let e=a();const t=e.init||{};e.init={...t}}(),s(),function(){let e=a();const t=e.loader_config||{};e.loader_config={...t}}(),a()}},2843:(e,t,r)=>{"use strict";r.d(t,{u:()=>i});var n=r(3878);function i(e,t=!1,r,i){(0,n.DD)("visibilitychange",(function(){if(t)return void("hidden"===document.visibilityState&&e());e(document.visibilityState)}),r,i)}},8139:(e,t,r)=>{"use strict";r.d(t,{u:()=>f});var n=r(7836),i=r(3434),o=r(8990),a=r(6154);const s={},c=a.gm.XMLHttpRequest,u="addEventListener",d="removeEventListener",l="nr@wrapped:".concat(n.P);function f(e){var t=function(e){return(e||n.ee).get("events")}(e);if(s[t.debugId]++)return t;s[t.debugId]=1;var r=(0,i.YM)(t,!0);function f(e){r.inPlace(e,[u,d],"-",p)}function p(e,t){return e[1]}return"getPrototypeOf"in Object&&(a.RI&&h(document,f),c&&h(c.prototype,f),h(a.gm,f)),t.on(u+"-start",(function(e,t){var n=e[1];if(null!==n&&("function"==typeof n||"object"==typeof n)){var i=(0,o.I)(n,l,(function(){var e={object:function(){if("function"!=typeof n.handleEvent)return;return n.handleEvent.apply(n,arguments)},function:n}[typeof n];return e?r(e,"fn-",null,e.name||"anonymous"):n}));this.wrapped=e[1]=i}})),t.on(d+"-start",(function(e){e[1]=this.wrapped||e[1]})),t}function h(e,t,...r){let n=e;for(;"object"==typeof n&&!Object.prototype.hasOwnProperty.call(n,u);)n=Object.getPrototypeOf(n);n&&t(n,...r)}},3434:(e,t,r)=>{"use strict";r.d(t,{Jt:()=>o,YM:()=>c});var n=r(7836),i=r(5607);const o="nr@original:".concat(i.W);var a=Object.prototype.hasOwnProperty,s=!1;function c(e,t){return e||(e=n.ee),r.inPlace=function(e,t,n,i,o){n||(n="");const a="-"===n.charAt(0);for(let s=0;s<t.length;s++){const c=t[s],u=e[c];d(u)||(e[c]=r(u,a?c+n:n,i,c,o))}},r.flag=o,r;function r(t,r,n,s,c){return d(t)?t:(r||(r=""),nrWrapper[o]=t,function(e,t,r){if(Object.defineProperty&&Object.keys)try{return Object.keys(e).forEach((function(r){Object.defineProperty(t,r,{get:function(){return e[r]},set:function(t){return e[r]=t,t}})})),t}catch(e){u([e],r)}for(var n in e)a.call(e,n)&&(t[n]=e[n])}(t,nrWrapper,e),nrWrapper);function nrWrapper(){var o,a,d,l;try{a=this,o=[...arguments],d="function"==typeof n?n(o,a):n||{}}catch(t){u([t,"",[o,a,s],d],e)}i(r+"start",[o,a,s],d,c);try{return l=t.apply(a,o)}catch(e){throw i(r+"err",[o,a,e],d,c),e}finally{i(r+"end",[o,a,l],d,c)}}}function i(r,n,i,o){if(!s||t){var a=s;s=!0;try{e.emit(r,n,i,t,o)}catch(t){u([t,r,n,i],e)}s=a}}}function u(e,t){t||(t=n.ee);try{t.emit("internal-error",e)}catch(e){}}function d(e){return!(e&&"function"==typeof e&&e.apply&&!e[o])}},9414:(e,t,r)=>{"use strict";r.d(t,{J:()=>c});var n=r(7836),i=r(2646),o=r(944),a=r(3434);const s=new Map;function c(e,t,r,c){if("object"!=typeof t||!t||"string"!=typeof r||!r||"function"!=typeof t[r])return(0,o.R)(29);const u=function(e){return(e||n.ee).get("logger")}(e),d=(0,a.YM)(u),l=new i.y(n.P);l.level=c.level,l.customAttributes=c.customAttributes;const f=t[r]?.[a.Jt]||t[r];return s.set(f,l),d.inPlace(t,[r],"wrap-logger-",(()=>s.get(f))),u}},9300:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.ajax},3333:(e,t,r)=>{"use strict";r.d(t,{$v:()=>u,TZ:()=>n,Zp:()=>i,kd:()=>c,mq:()=>s,nf:()=>a,qN:()=>o});const n=r(860).K7.genericEvents,i=["auxclick","click","copy","keydown","paste","scrollend"],o=["focus","blur"],a=4,s=1e3,c=["PageAction","UserAction","BrowserPerformance"],u={MARKS:"experimental.marks",MEASURES:"experimental.measures",RESOURCES:"experimental.resources"}},6774:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.jserrors},993:(e,t,r)=>{"use strict";r.d(t,{A$:()=>o,ET:()=>a,TZ:()=>s,p_:()=>i});var n=r(860);const i={ERROR:"ERROR",WARN:"WARN",INFO:"INFO",DEBUG:"DEBUG",TRACE:"TRACE"},o={OFF:0,ERROR:1,WARN:2,INFO:3,DEBUG:4,TRACE:5},a="log",s=n.K7.logging},3785:(e,t,r)=>{"use strict";r.d(t,{R:()=>c,b:()=>u});var n=r(9908),i=r(1863),o=r(860),a=r(8154),s=r(993);function c(e,t,r={},c=s.p_.INFO){(0,n.p)(a.xV,["API/logging/".concat(c.toLowerCase(),"/called")],void 0,o.K7.metrics,e),(0,n.p)(s.ET,[(0,i.t)(),t,r,c],void 0,o.K7.logging,e)}function u(e){return"string"==typeof e&&Object.values(s.p_).some((t=>t===e.toUpperCase().trim()))}},8154:(e,t,r)=>{"use strict";r.d(t,{z_:()=>o,XG:()=>s,TZ:()=>n,rs:()=>i,xV:()=>a});r(6154),r(9566),r(384);const n=r(860).K7.metrics,i="sm",o="cm",a="storeSupportabilityMetrics",s="storeEventMetrics"},6630:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewEvent},782:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewTiming},6344:(e,t,r)=>{"use strict";r.d(t,{BB:()=>d,G4:()=>o,Qb:()=>l,TZ:()=>i,Ug:()=>a,_s:()=>s,bc:()=>u,yP:()=>c});var n=r(2614);const i=r(860).K7.sessionReplay,o={RECORD:"recordReplay",PAUSE:"pauseReplay",REPLAY_RUNNING:"replayRunning",ERROR_DURING_REPLAY:"errorDuringReplay"},a=.12,s={DomContentLoaded:0,Load:1,FullSnapshot:2,IncrementalSnapshot:3,Meta:4,Custom:5},c={[n.g.ERROR]:15e3,[n.g.FULL]:3e5,[n.g.OFF]:0},u={RESET:{message:"Session was reset",sm:"Reset"},IMPORT:{message:"Recorder failed to import",sm:"Import"},TOO_MANY:{message:"429: Too Many Requests",sm:"Too-Many"},TOO_BIG:{message:"Payload was too large",sm:"Too-Big"},CROSS_TAB:{message:"Session Entity was set to OFF on another tab",sm:"Cross-Tab"},ENTITLEMENTS:{message:"Session Replay is not allowed and will not be started",sm:"Entitlement"}},d=5e3,l={API:"api"}},5270:(e,t,r)=>{"use strict";r.d(t,{Aw:()=>c,CT:()=>u,SR:()=>s});var n=r(384),i=r(9417),o=r(7767),a=r(6154);function s(e){return!!(0,n.dV)().o.MO&&(0,o.V)(e)&&!0===(0,i.gD)(e,"session_trace.enabled")}function c(e){return!0===(0,i.gD)(e,"session_replay.preload")&&s(e)}function u(e,t){const r=t.correctAbsoluteTimestamp(e);return{originalTimestamp:e,correctedTimestamp:r,timestampDiff:e-r,originTime:a.WN,correctedOriginTime:t.correctedOriginTime,originTimeDiff:Math.floor(a.WN-t.correctedOriginTime)}}},3738:(e,t,r)=>{"use strict";r.d(t,{He:()=>i,Kp:()=>s,Lc:()=>u,Rz:()=>d,TZ:()=>n,bD:()=>o,d3:()=>a,jx:()=>l,uP:()=>c});const n=r(860).K7.sessionTrace,i="bstResource",o="resource",a="-start",s="-end",c="fn"+a,u="fn"+s,d="pushState",l=1e3},3962:(e,t,r)=>{"use strict";r.d(t,{AM:()=>o,O2:()=>c,Qu:()=>u,TZ:()=>s,ih:()=>d,pP:()=>a,tC:()=>i});var n=r(860);const i=["click","keydown","submit","popstate"],o="api",a="initialPageLoad",s=n.K7.softNav,c={INITIAL_PAGE_LOAD:"",ROUTE_CHANGE:1,UNSPECIFIED:2},u={INTERACTION:1,AJAX:2,CUSTOM_END:3,CUSTOM_TRACER:4},d={IP:"in progress",FIN:"finished",CAN:"cancelled"}},7378:(e,t,r)=>{"use strict";r.d(t,{$p:()=>x,BR:()=>b,Kp:()=>R,L3:()=>y,Lc:()=>c,NC:()=>o,SG:()=>d,TZ:()=>i,U6:()=>p,UT:()=>m,d3:()=>w,dT:()=>f,e5:()=>A,gx:()=>v,l9:()=>l,oW:()=>h,op:()=>g,rw:()=>u,tH:()=>T,uP:()=>s,wW:()=>E,xq:()=>a});var n=r(384);const i=r(860).K7.spa,o=["click","submit","keypress","keydown","keyup","change"],a=999,s="fn-start",c="fn-end",u="cb-start",d="api-ixn-",l="remaining",f="interaction",h="spaNode",p="jsonpNode",g="fetch-start",m="fetch-done",v="fetch-body-",b="jsonp-end",y=(0,n.dV)().o.ST,w="-start",R="-end",x="-body",E="cb"+R,A="jsTime",T="fetch"},4234:(e,t,r)=>{"use strict";r.d(t,{W:()=>o});var n=r(7836),i=r(1687);class o{constructor(e,t){this.agentIdentifier=e,this.ee=n.ee.get(e),this.featureName=t,this.blocked=!1}deregisterDrain(){(0,i.x3)(this.agentIdentifier,this.featureName)}}},7767:(e,t,r)=>{"use strict";r.d(t,{V:()=>o});var n=r(9417),i=r(6154);const o=e=>i.RI&&!0===(0,n.gD)(e,"privacy.cookies_enabled")},8969:(e,t,r)=>{"use strict";r.d(t,{j:()=>O});var n=r(860),i=r(2555),o=r(3371),a=r(9908),s=r(7836),c=r(1687),u=r(5289),d=r(6154),l=r(944),f=r(8154),h=r(384),p=r(6344);const g=["setErrorHandler","finished","addToTrace","addRelease","recordCustomEvent","addPageAction","setCurrentRouteName","setPageViewName","setCustomAttribute","interaction","noticeError","setUserId","setApplicationVersion","start",p.G4.RECORD,p.G4.PAUSE,"log","wrapLogger"],m=["setErrorHandler","finished","addToTrace","addRelease"];var v=r(1863),b=r(2614),y=r(993),w=r(3785),R=r(9414);function x(){const e=(0,h.pV)();g.forEach((t=>{e[t]=(...r)=>function(t,...r){let n=[];return Object.values(e.initializedAgents).forEach((e=>{e&&e.api?e.exposed&&e.api[t]&&n.push(e.api[t](...r)):(0,l.R)(38,t)})),n.length>1?n:n[0]}(t,...r)}))}const E={};var A=r(9417),T=r(5603),N=r(5284);const S=e=>{const t=e.startsWith("http");e+="/",r.p=t?e:"https://"+e};let _=!1;function O(e,t={},g,O){let{init:I,info:P,loader_config:j,runtime:C={},exposed:k=!0}=t;C.loaderType=g;const L=(0,h.pV)();P||(I=L.init,P=L.info,j=L.loader_config),(0,A.xN)(e.agentIdentifier,I||{}),(0,T.a)(e.agentIdentifier,j||{}),P.jsAttributes??={},d.bv&&(P.jsAttributes.isWorker=!0),(0,i.x1)(e.agentIdentifier,P);const H=(0,A.D0)(e.agentIdentifier),M=[P.beacon,P.errorBeacon];_||(H.proxy.assets&&(S(H.proxy.assets),M.push(H.proxy.assets)),H.proxy.beacon&&M.push(H.proxy.beacon),x(),(0,h.US)("activatedFeatures",N.B),e.runSoftNavOverSpa&&=!0===H.soft_navigations.enabled&&H.feature_flags.includes("soft_nav")),C.denyList=[...H.ajax.deny_list||[],...H.ajax.block_internal?M:[]],C.ptid=e.agentIdentifier,(0,o.V)(e.agentIdentifier,C),e.ee=s.ee.get(e.agentIdentifier),void 0===e.api&&(e.api=function(e,t,h=!1){t||(0,c.Ak)(e,"api");const g={};var x=s.ee.get(e),A=x.get("tracer");E[e]=b.g.OFF,x.on(p.G4.REPLAY_RUNNING,(t=>{E[e]=t}));var T="api-",N=T+"ixn-";function S(t,r,n,o){const a=(0,i.Vp)(e);return null===r?delete a.jsAttributes[t]:(0,i.x1)(e,{...a,jsAttributes:{...a.jsAttributes,[t]:r}}),I(T,n,!0,o||null===r?"session":void 0)(t,r)}function _(){}g.log=function(e,{customAttributes:t={},level:r=y.p_.INFO}={}){(0,a.p)(f.xV,["API/log/called"],void 0,n.K7.metrics,x),(0,w.R)(x,e,t,r)},g.wrapLogger=(e,t,{customAttributes:r={},level:i=y.p_.INFO}={})=>{(0,a.p)(f.xV,["API/wrapLogger/called"],void 0,n.K7.metrics,x),(0,R.J)(x,e,t,{customAttributes:r,level:i})},m.forEach((e=>{g[e]=I(T,e,!0,"api")})),g.addPageAction=I(T,"addPageAction",!0,n.K7.genericEvents),g.recordCustomEvent=I(T,"recordCustomEvent",!0,n.K7.genericEvents),g.setPageViewName=function(t,r){if("string"==typeof t)return"/"!==t.charAt(0)&&(t="/"+t),(0,o.f)(e).customTransaction=(r||"http://custom.transaction")+t,I(T,"setPageViewName",!0)()},g.setCustomAttribute=function(e,t,r=!1){if("string"==typeof e){if(["string","number","boolean"].includes(typeof t)||null===t)return S(e,t,"setCustomAttribute",r);(0,l.R)(40,typeof t)}else(0,l.R)(39,typeof e)},g.setUserId=function(e){if("string"==typeof e||null===e)return S("enduser.id",e,"setUserId",!0);(0,l.R)(41,typeof e)},g.setApplicationVersion=function(e){if("string"==typeof e||null===e)return S("application.version",e,"setApplicationVersion",!1);(0,l.R)(42,typeof e)},g.start=()=>{try{(0,a.p)(f.xV,["API/start/called"],void 0,n.K7.metrics,x),x.emit("manual-start-all")}catch(e){(0,l.R)(23,e)}},g[p.G4.RECORD]=function(){(0,a.p)(f.xV,["API/recordReplay/called"],void 0,n.K7.metrics,x),(0,a.p)(p.G4.RECORD,[],void 0,n.K7.sessionReplay,x)},g[p.G4.PAUSE]=function(){(0,a.p)(f.xV,["API/pauseReplay/called"],void 0,n.K7.metrics,x),(0,a.p)(p.G4.PAUSE,[],void 0,n.K7.sessionReplay,x)},g.interaction=function(e){return(new _).get("object"==typeof e?e:{})};const O=_.prototype={createTracer:function(e,t){var r={},i=this,o="function"==typeof t;return(0,a.p)(f.xV,["API/createTracer/called"],void 0,n.K7.metrics,x),h||(0,a.p)(N+"tracer",[(0,v.t)(),e,r],i,n.K7.spa,x),function(){if(A.emit((o?"":"no-")+"fn-start",[(0,v.t)(),i,o],r),o)try{return t.apply(this,arguments)}catch(e){const t="string"==typeof e?new Error(e):e;throw A.emit("fn-err",[arguments,this,t],r),t}finally{A.emit("fn-end",[(0,v.t)()],r)}}}};function I(e,t,r,i){return function(){return(0,a.p)(f.xV,["API/"+t+"/called"],void 0,n.K7.metrics,x),i&&(0,a.p)(e+t,[r?(0,v.t)():performance.now(),...arguments],r?null:this,i,x),r?void 0:this}}function P(){r.e(478).then(r.bind(r,8778)).then((({setAPI:t})=>{t(e),(0,c.Ze)(e,"api")})).catch((e=>{(0,l.R)(27,e),x.abort()}))}return["actionText","setName","setAttribute","save","ignore","onEnd","getContext","end","get"].forEach((e=>{O[e]=I(N,e,void 0,h?n.K7.softNav:n.K7.spa)})),g.setCurrentRouteName=h?I(N,"routeName",void 0,n.K7.softNav):I(T,"routeName",!0,n.K7.spa),g.noticeError=function(t,r){"string"==typeof t&&(t=new Error(t)),(0,a.p)(f.xV,["API/noticeError/called"],void 0,n.K7.metrics,x),(0,a.p)("err",[t,(0,v.t)(),!1,r,!!E[e]],void 0,n.K7.jserrors,x)},d.RI?(0,u.GG)((()=>P()),!0):P(),g}(e.agentIdentifier,O,e.runSoftNavOverSpa)),void 0===e.exposed&&(e.exposed=k),_=!0}},8374:(e,t,r)=>{r.nc=(()=>{try{return document?.currentScript?.nonce}catch(e){}return""})()},860:(e,t,r)=>{"use strict";r.d(t,{$J:()=>u,K7:()=>s,P3:()=>c,XX:()=>i,qY:()=>n,v4:()=>a});const n="events",i="jserrors",o="browser/blobs",a="rum",s={ajax:"ajax",genericEvents:"generic_events",jserrors:i,logging:"logging",metrics:"metrics",pageAction:"page_action",pageViewEvent:"page_view_event",pageViewTiming:"page_view_timing",sessionReplay:"session_replay",sessionTrace:"session_trace",softNav:"soft_navigations",spa:"spa"},c={[s.pageViewEvent]:1,[s.pageViewTiming]:2,[s.metrics]:3,[s.jserrors]:4,[s.spa]:5,[s.ajax]:6,[s.sessionTrace]:7,[s.softNav]:8,[s.sessionReplay]:9,[s.logging]:10,[s.genericEvents]:11},u={[s.pageViewEvent]:a,[s.pageViewTiming]:n,[s.ajax]:n,[s.spa]:n,[s.softNav]:n,[s.metrics]:i,[s.jserrors]:i,[s.sessionTrace]:o,[s.sessionReplay]:o,[s.logging]:"browser/logs",[s.genericEvents]:"ins"}}},n={};function i(e){var t=n[e];if(void 0!==t)return t.exports;var o=n[e]={exports:{}};return r[e](o,o.exports,i),o.exports}i.m=r,i.d=(e,t)=>{for(var r in t)i.o(t,r)&&!i.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,r)=>(i.f[r](e,t),t)),[])),i.u=e=>({212:"nr-spa-compressor",249:"nr-spa-recorder",478:"nr-spa"}[e]+"-1.283.2.min.js"),i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA-1.283.2.PROD:",i.l=(r,n,o,a)=>{if(e[r])e[r].push(n);else{var s,c;if(void 0!==o)for(var u=document.getElementsByTagName("script"),d=0;d<u.length;d++){var l=u[d];if(l.getAttribute("src")==r||l.getAttribute("data-webpack")==t+o){s=l;break}}if(!s){c=!0;var f={478:"sha512-2oN05BjxuObKuOX8E0vq/zS51M+2HokmNPBRUrIC1fw3hpJqoI18/nckSFiqV11KxT7ag3C+FunKrR8n0PD9Ig==",249:"sha512-Zs5nIHr/khH6G8IhAEdnngg+P7y/IfmjU0PQmXABpCEtSTeKV22OYdaa9lENrW9uxI0lZ6O5e5dCnEMsTS0onA==",212:"sha512-LPKde7A1ZxIHzoSqWKxn5uWVhM9u76Vtmp9DMBf+Ry3mnn2jpsfyfigMYD5Yka2RG3NeIBqOwNYuPrWL39qn6w=="};(s=document.createElement("script")).charset="utf-8",s.timeout=120,i.nc&&s.setAttribute("nonce",i.nc),s.setAttribute("data-webpack",t+o),s.src=r,0!==s.src.indexOf(window.location.origin+"/")&&(s.crossOrigin="anonymous"),f[a]&&(s.integrity=f[a])}e[r]=[n];var h=(t,n)=>{s.onerror=s.onload=null,clearTimeout(p);var i=e[r];if(delete e[r],s.parentNode&&s.parentNode.removeChild(s),i&&i.forEach((e=>e(n))),t)return t(n)},p=setTimeout(h.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=h.bind(null,s.onerror),s.onload=h.bind(null,s.onload),c&&document.head.appendChild(s)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.p="https://js-agent.newrelic.com/",(()=>{var e={38:0,788:0};i.f.j=(t,r)=>{var n=i.o(e,t)?e[t]:void 0;if(0!==n)if(n)r.push(n[2]);else{var o=new Promise(((r,i)=>n=e[t]=[r,i]));r.push(n[2]=o);var a=i.p+i.u(t),s=new Error;i.l(a,(r=>{if(i.o(e,t)&&(0!==(n=e[t])&&(e[t]=void 0),n)){var o=r&&("load"===r.type?"missing":r.type),a=r&&r.target&&r.target.src;s.message="Loading chunk "+t+" failed.\n("+o+": "+a+")",s.name="ChunkLoadError",s.type=o,s.request=a,n[1](s)}}),"chunk-"+t,t)}};var t=(t,r)=>{var n,o,[a,s,c]=r,u=0;if(a.some((t=>0!==e[t]))){for(n in s)i.o(s,n)&&(i.m[n]=s[n]);if(c)c(i)}for(t&&t(r);u<a.length;u++)o=a[u],i.o(e,o)&&e[o]&&e[o][0](),e[o]=0},r=self["webpackChunk:NRBA-1.283.2.PROD"]=self["webpackChunk:NRBA-1.283.2.PROD"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),(()=>{"use strict";i(8374);var e=i(944),t=i(6344),r=i(9566);class n{agentIdentifier;constructor(){this.agentIdentifier=(0,r.LA)(16)}#e(t,...r){if("function"==typeof this.api?.[t])return this.api[t](...r);(0,e.R)(35,t)}addPageAction(e,t){return this.#e("addPageAction",e,t)}recordCustomEvent(e,t){return this.#e("recordCustomEvent",e,t)}setPageViewName(e,t){return this.#e("setPageViewName",e,t)}setCustomAttribute(e,t,r){return this.#e("setCustomAttribute",e,t,r)}noticeError(e,t){return this.#e("noticeError",e,t)}setUserId(e){return this.#e("setUserId",e)}setApplicationVersion(e){return this.#e("setApplicationVersion",e)}setErrorHandler(e){return this.#e("setErrorHandler",e)}addRelease(e,t){return this.#e("addRelease",e,t)}log(e,t){return this.#e("log",e,t)}}class o extends n{#e(t,...r){if("function"==typeof this.api?.[t])return this.api[t](...r);(0,e.R)(35,t)}start(){return this.#e("start")}finished(e){return this.#e("finished",e)}recordReplay(){return this.#e(t.G4.RECORD)}pauseReplay(){return this.#e(t.G4.PAUSE)}addToTrace(e){return this.#e("addToTrace",e)}setCurrentRouteName(e){return this.#e("setCurrentRouteName",e)}interaction(){return this.#e("interaction")}wrapLogger(e,t,r){return this.#e("wrapLogger",e,t,r)}}var a=i(860),s=i(9417);const c=Object.values(a.K7);function u(e){const t={};return c.forEach((r=>{t[r]=function(e,t){return!0===(0,s.gD)(t,"".concat(e,".enabled"))}(r,e)})),t}var d=i(8969);var l=i(1687),f=i(4234),h=i(5289),p=i(6154),g=i(5270),m=i(7767),v=i(6389);class b extends f.W{constructor(e,t,r=!0){super(e.agentIdentifier,t),this.auto=r,this.abortHandler=void 0,this.featAggregate=void 0,this.onAggregateImported=void 0,!1===e.init[this.featureName].autoStart&&(this.auto=!1),this.auto?(0,l.Ak)(e.agentIdentifier,t):this.ee.on("manual-start-all",(0,v.J)((()=>{(0,l.Ak)(e.agentIdentifier,this.featureName),this.auto=!0,this.importAggregator(e)})))}importAggregator(t,r={}){if(this.featAggregate||!this.auto)return;let n;this.onAggregateImported=new Promise((e=>{n=e}));const o=async()=>{let o;try{if((0,m.V)(this.agentIdentifier)){const{setupAgentSession:e}=await i.e(478).then(i.bind(i,6526));o=e(t)}}catch(t){(0,e.R)(20,t),this.ee.emit("internal-error",[t]),this.featureName===a.K7.sessionReplay&&this.abortHandler?.()}try{if(!this.#t(this.featureName,o))return(0,l.Ze)(this.agentIdentifier,this.featureName),void n(!1);const{lazyFeatureLoader:e}=await i.e(478).then(i.bind(i,6103)),{Aggregate:a}=await e(this.featureName,"aggregate");this.featAggregate=new a(t,r),t.runtime.harvester.initializedAggregates.push(this.featAggregate),n(!0)}catch(t){(0,e.R)(34,t),this.abortHandler?.(),(0,l.Ze)(this.agentIdentifier,this.featureName,!0),n(!1),this.ee&&this.ee.abort()}};p.RI?(0,h.GG)((()=>o()),!0):o()}#t(e,t){switch(e){case a.K7.sessionReplay:return(0,g.SR)(this.agentIdentifier)&&!!t;case a.K7.sessionTrace:return!!t;default:return!0}}}var y=i(6630);class w extends b{static featureName=y.T;constructor(e,t=!0){super(e,y.T,t),this.importAggregator(e)}}var R=i(384);var x=i(9908),E=i(2843),A=i(3878),T=i(782),N=i(1863);class S extends b{static featureName=T.T;constructor(e,t=!0){super(e,T.T,t),p.RI&&((0,E.u)((()=>(0,x.p)("docHidden",[(0,N.t)()],void 0,T.T,this.ee)),!0),(0,A.sp)("pagehide",(()=>(0,x.p)("winPagehide",[(0,N.t)()],void 0,T.T,this.ee))),this.importAggregator(e))}}var _=i(8154);class O extends b{static featureName=_.TZ;constructor(e,t=!0){super(e,_.TZ,t),this.importAggregator(e)}}var I=i(6774),P=i(3304);class j{constructor(e,t,r,n,i){this.name="UncaughtError",this.message="string"==typeof e?e:(0,P.A)(e),this.sourceURL=t,this.line=r,this.column=n,this.__newrelic=i}}function C(e){return H(e)?e:new j(void 0!==e?.message?e.message:e,e?.filename||e?.sourceURL,e?.lineno||e?.line,e?.colno||e?.col,e?.__newrelic)}function k(e){const t="Unhandled Promise Rejection";if(!e?.reason)return;if(H(e.reason))try{return e.reason.message=t+": "+e.reason.message,C(e.reason)}catch(t){return C(e.reason)}const r=C(e.reason);return r.message=t+": "+r?.message,r}function L(e){if(e.error instanceof SyntaxError&&!/:\d+$/.test(e.error.stack?.trim())){const t=new j(e.message,e.filename,e.lineno,e.colno,e.error.__newrelic);return t.name=SyntaxError.name,t}return H(e.error)?e.error:C(e)}function H(e){return e instanceof Error&&!!e.stack}class M extends b{static featureName=I.T;#r=!1;constructor(e,r=!0){super(e,I.T,r);try{this.removeOnAbort=new AbortController}catch(e){}this.ee.on("internal-error",((e,t)=>{this.abortHandler&&(0,x.p)("ierr",[C(e),(0,N.t)(),!0,{},this.#r,t],void 0,this.featureName,this.ee)})),this.ee.on(t.G4.REPLAY_RUNNING,(e=>{this.#r=e})),p.gm.addEventListener("unhandledrejection",(e=>{this.abortHandler&&(0,x.p)("err",[k(e),(0,N.t)(),!1,{unhandledPromiseRejection:1},this.#r],void 0,this.featureName,this.ee)}),(0,A.jT)(!1,this.removeOnAbort?.signal)),p.gm.addEventListener("error",(e=>{this.abortHandler&&(0,x.p)("err",[L(e),(0,N.t)(),!1,{},this.#r],void 0,this.featureName,this.ee)}),(0,A.jT)(!1,this.removeOnAbort?.signal)),this.abortHandler=this.#n,this.importAggregator(e)}#n(){this.removeOnAbort?.abort(),this.abortHandler=void 0}}var D=i(8990);let K=1;const U="nr@id";function V(e){const t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===p.gm?0:(0,D.I)(e,U,(function(){return K++}))}function G(e){if("string"==typeof e&&e.length)return e.length;if("object"==typeof e){if("undefined"!=typeof ArrayBuffer&&e instanceof ArrayBuffer&&e.byteLength)return e.byteLength;if("undefined"!=typeof Blob&&e instanceof Blob&&e.size)return e.size;if(!("undefined"!=typeof FormData&&e instanceof FormData))try{return(0,P.A)(e).length}catch(e){return}}}var F=i(8139),B=i(7836),W=i(3434);const z={},q=["open","send"];function Z(t){var r=t||B.ee;const n=function(e){return(e||B.ee).get("xhr")}(r);if(void 0===p.gm.XMLHttpRequest)return n;if(z[n.debugId]++)return n;z[n.debugId]=1,(0,F.u)(r);var i=(0,W.YM)(n),o=p.gm.XMLHttpRequest,a=p.gm.MutationObserver,s=p.gm.Promise,c=p.gm.setInterval,u="readystatechange",d=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],l=[],f=p.gm.XMLHttpRequest=function(t){const r=new o(t),a=n.context(r);try{n.emit("new-xhr",[r],a),r.addEventListener(u,(s=a,function(){var e=this;e.readyState>3&&!s.resolved&&(s.resolved=!0,n.emit("xhr-resolved",[],e)),i.inPlace(e,d,"fn-",y)}),(0,A.jT)(!1))}catch(t){(0,e.R)(15,t);try{n.emit("internal-error",[t])}catch(e){}}var s;return r};function h(e,t){i.inPlace(t,["onreadystatechange"],"fn-",y)}if(function(e,t){for(var r in e)t[r]=e[r]}(o,f),f.prototype=o.prototype,i.inPlace(f.prototype,q,"-xhr-",y),n.on("send-xhr-start",(function(e,t){h(e,t),function(e){l.push(e),a&&(g?g.then(b):c?c(b):(m=-m,v.data=m))}(t)})),n.on("open-xhr-start",h),a){var g=s&&s.resolve();if(!c&&!s){var m=1,v=document.createTextNode(m);new a(b).observe(v,{characterData:!0})}}else r.on("fn-end",(function(e){e[0]&&e[0].type===u||b()}));function b(){for(var e=0;e<l.length;e++)h(0,l[e]);l.length&&(l=[])}function y(e,t){return t}return n}var Y="fetch-",J=Y+"body-",X=["arrayBuffer","blob","json","text","formData"],Q=p.gm.Request,ee=p.gm.Response,te="prototype";const re={};function ne(e){const t=function(e){return(e||B.ee).get("fetch")}(e);if(!(Q&&ee&&p.gm.fetch))return t;if(re[t.debugId]++)return t;function r(e,r,n){var i=e[r];"function"==typeof i&&(e[r]=function(){var e,r=[...arguments],o={};t.emit(n+"before-start",[r],o),o[B.P]&&o[B.P].dt&&(e=o[B.P].dt);var a=i.apply(this,r);return t.emit(n+"start",[r,e],a),a.then((function(e){return t.emit(n+"end",[null,e],a),e}),(function(e){throw t.emit(n+"end",[e],a),e}))})}return re[t.debugId]=1,X.forEach((e=>{r(Q[te],e,J),r(ee[te],e,J)})),r(p.gm,"fetch",Y),t.on(Y+"end",(function(e,r){var n=this;if(r){var i=r.headers.get("content-length");null!==i&&(n.rxSize=i),t.emit(Y+"done",[null,r],n)}else t.emit(Y+"done",[e],n)})),t}var ie=i(7485),oe=i(5603);class ae{constructor(e){this.agentIdentifier=e}generateTracePayload(e){if(!this.shouldGenerateTrace(e))return null;var t=(0,oe.o)(this.agentIdentifier);if(!t)return null;var n=(t.accountID||"").toString()||null,i=(t.agentID||"").toString()||null,o=(t.trustKey||"").toString()||null;if(!n||!i)return null;var a=(0,r.ZF)(),s=(0,r.el)(),c=Date.now(),u={spanId:a,traceId:s,timestamp:c};return(e.sameOrigin||this.isAllowedOrigin(e)&&this.useTraceContextHeadersForCors())&&(u.traceContextParentHeader=this.generateTraceContextParentHeader(a,s),u.traceContextStateHeader=this.generateTraceContextStateHeader(a,c,n,i,o)),(e.sameOrigin&&!this.excludeNewrelicHeader()||!e.sameOrigin&&this.isAllowedOrigin(e)&&this.useNewrelicHeaderForCors())&&(u.newrelicHeader=this.generateTraceHeader(a,s,c,n,i,o)),u}generateTraceContextParentHeader(e,t){return"00-"+t+"-"+e+"-01"}generateTraceContextStateHeader(e,t,r,n,i){return i+"@nr=0-1-"+r+"-"+n+"-"+e+"----"+t}generateTraceHeader(e,t,r,n,i,o){if(!("function"==typeof p.gm?.btoa))return null;var a={v:[0,1],d:{ty:"Browser",ac:n,ap:i,id:e,tr:t,ti:r}};return o&&n!==o&&(a.d.tk=o),btoa((0,P.A)(a))}shouldGenerateTrace(e){return this.isDtEnabled()&&this.isAllowedOrigin(e)}isAllowedOrigin(e){var t=!1,r={};if((0,s.gD)(this.agentIdentifier,"distributed_tracing")&&(r=(0,s.D0)(this.agentIdentifier).distributed_tracing),e.sameOrigin)t=!0;else if(r.allowed_origins instanceof Array)for(var n=0;n<r.allowed_origins.length;n++){var i=(0,ie.D)(r.allowed_origins[n]);if(e.hostname===i.hostname&&e.protocol===i.protocol&&e.port===i.port){t=!0;break}}return t}isDtEnabled(){var e=(0,s.gD)(this.agentIdentifier,"distributed_tracing");return!!e&&!!e.enabled}excludeNewrelicHeader(){var e=(0,s.gD)(this.agentIdentifier,"distributed_tracing");return!!e&&!!e.exclude_newrelic_header}useNewrelicHeaderForCors(){var e=(0,s.gD)(this.agentIdentifier,"distributed_tracing");return!!e&&!1!==e.cors_use_newrelic_header}useTraceContextHeadersForCors(){var e=(0,s.gD)(this.agentIdentifier,"distributed_tracing");return!!e&&!!e.cors_use_tracecontext_headers}}var se=i(9300),ce=i(7295),ue=["load","error","abort","timeout"],de=ue.length,le=(0,R.dV)().o.REQ,fe=(0,R.dV)().o.XHR;class he extends b{static featureName=se.T;constructor(e,t=!0){super(e,se.T,t),this.dt=new ae(e.agentIdentifier),this.handler=(e,t,r,n)=>(0,x.p)(e,t,r,n,this.ee);try{const e={xmlhttprequest:"xhr",fetch:"fetch",beacon:"beacon"};p.gm?.performance?.getEntriesByType("resource").forEach((t=>{if(t.initiatorType in e&&0!==t.responseStatus){const r={status:t.responseStatus},n={rxSize:t.transferSize,duration:Math.floor(t.duration),cbTime:0};pe(r,t.name),this.handler("xhr",[r,n,t.startTime,t.responseEnd,e[t.initiatorType]],void 0,a.K7.ajax)}}))}catch(e){}ne(this.ee),Z(this.ee),function(e,t,r,n){function i(e){var t=this;t.totalCbs=0,t.called=0,t.cbTime=0,t.end=R,t.ended=!1,t.xhrGuids={},t.lastSize=null,t.loadCaptureCalled=!1,t.params=this.params||{},t.metrics=this.metrics||{},e.addEventListener("load",(function(r){E(t,e)}),(0,A.jT)(!1)),p.lR||e.addEventListener("progress",(function(e){t.lastSize=e.loaded}),(0,A.jT)(!1))}function o(e){this.params={method:e[0]},pe(this,e[1]),this.metrics={}}function s(t,r){e.loader_config.xpid&&this.sameOrigin&&r.setRequestHeader("X-NewRelic-ID",e.loader_config.xpid);var i=n.generateTracePayload(this.parsedOrigin);if(i){var o=!1;i.newrelicHeader&&(r.setRequestHeader("newrelic",i.newrelicHeader),o=!0),i.traceContextParentHeader&&(r.setRequestHeader("traceparent",i.traceContextParentHeader),i.traceContextStateHeader&&r.setRequestHeader("tracestate",i.traceContextStateHeader),o=!0),o&&(this.dt=i)}}function c(e,r){var n=this.metrics,i=e[0],o=this;if(n&&i){var a=G(i);a&&(n.txSize=a)}this.startTime=(0,N.t)(),this.body=i,this.listener=function(e){try{"abort"!==e.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==e.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof r.onload)&&"function"==typeof o.end)&&o.end(r)}catch(e){try{t.emit("internal-error",[e])}catch(e){}}};for(var s=0;s<de;s++)r.addEventListener(ue[s],this.listener,(0,A.jT)(!1))}function u(e,t,r){this.cbTime+=e,t?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof r.onload||"function"!=typeof this.end||this.end(r)}function d(e,t){var r=""+V(e)+!!t;this.xhrGuids&&!this.xhrGuids[r]&&(this.xhrGuids[r]=!0,this.totalCbs+=1)}function l(e,t){var r=""+V(e)+!!t;this.xhrGuids&&this.xhrGuids[r]&&(delete this.xhrGuids[r],this.totalCbs-=1)}function f(){this.endTime=(0,N.t)()}function h(e,r){r instanceof fe&&"load"===e[0]&&t.emit("xhr-load-added",[e[1],e[2]],r)}function g(e,r){r instanceof fe&&"load"===e[0]&&t.emit("xhr-load-removed",[e[1],e[2]],r)}function m(e,t,r){t instanceof fe&&("onload"===r&&(this.onload=!0),("load"===(e[0]&&e[0].type)||this.onload)&&(this.xhrCbStart=(0,N.t)()))}function v(e,r){this.xhrCbStart&&t.emit("xhr-cb-time",[(0,N.t)()-this.xhrCbStart,this.onload,r],r)}function b(e){var t,r=e[1]||{};if("string"==typeof e[0]?0===(t=e[0]).length&&p.RI&&(t=""+p.gm.location.href):e[0]&&e[0].url?t=e[0].url:p.gm?.URL&&e[0]&&e[0]instanceof URL?t=e[0].href:"function"==typeof e[0].toString&&(t=e[0].toString()),"string"==typeof t&&0!==t.length){t&&(this.parsedOrigin=(0,ie.D)(t),this.sameOrigin=this.parsedOrigin.sameOrigin);var i=n.generateTracePayload(this.parsedOrigin);if(i&&(i.newrelicHeader||i.traceContextParentHeader))if(e[0]&&e[0].headers)s(e[0].headers,i)&&(this.dt=i);else{var o={};for(var a in r)o[a]=r[a];o.headers=new Headers(r.headers||{}),s(o.headers,i)&&(this.dt=i),e.length>1?e[1]=o:e.push(o)}}function s(e,t){var r=!1;return t.newrelicHeader&&(e.set("newrelic",t.newrelicHeader),r=!0),t.traceContextParentHeader&&(e.set("traceparent",t.traceContextParentHeader),t.traceContextStateHeader&&e.set("tracestate",t.traceContextStateHeader),r=!0),r}}function y(e,t){this.params={},this.metrics={},this.startTime=(0,N.t)(),this.dt=t,e.length>=1&&(this.target=e[0]),e.length>=2&&(this.opts=e[1]);var r,n=this.opts||{},i=this.target;"string"==typeof i?r=i:"object"==typeof i&&i instanceof le?r=i.url:p.gm?.URL&&"object"==typeof i&&i instanceof URL&&(r=i.href),pe(this,r);var o=(""+(i&&i instanceof le&&i.method||n.method||"GET")).toUpperCase();this.params.method=o,this.body=n.body,this.txSize=G(n.body)||0}function w(e,t){if(this.endTime=(0,N.t)(),this.params||(this.params={}),(0,ce.iW)(this.params))return;let n;this.params.status=t?t.status:0,"string"==typeof this.rxSize&&this.rxSize.length>0&&(n=+this.rxSize);const i={txSize:this.txSize,rxSize:n,duration:(0,N.t)()-this.startTime};r("xhr",[this.params,i,this.startTime,this.endTime,"fetch"],this,a.K7.ajax)}function R(e){const t=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(let t=0;t<de;t++)e.removeEventListener(ue[t],this.listener,!1);t.aborted||(0,ce.iW)(t)||(n.duration=(0,N.t)()-this.startTime,this.loadCaptureCalled||4!==e.readyState?null==t.status&&(t.status=0):E(this,e),n.cbTime=this.cbTime,r("xhr",[t,n,this.startTime,this.endTime,"xhr"],this,a.K7.ajax))}}function E(e,r){e.params.status=r.status;var n=function(e,t){var r=e.responseType;return"json"===r&&null!==t?t:"arraybuffer"===r||"blob"===r||"json"===r?G(e.response):"text"===r||""===r||void 0===r?G(e.responseText):void 0}(r,e.lastSize);if(n&&(e.metrics.rxSize=n),e.sameOrigin){var i=r.getResponseHeader("X-NewRelic-App-Data");i&&((0,x.p)(_.rs,["Ajax/CrossApplicationTracing/Header/Seen"],void 0,a.K7.metrics,t),e.params.cat=i.split(", ").pop())}e.loadCaptureCalled=!0}t.on("new-xhr",i),t.on("open-xhr-start",o),t.on("open-xhr-end",s),t.on("send-xhr-start",c),t.on("xhr-cb-time",u),t.on("xhr-load-added",d),t.on("xhr-load-removed",l),t.on("xhr-resolved",f),t.on("addEventListener-end",h),t.on("removeEventListener-end",g),t.on("fn-end",v),t.on("fetch-before-start",b),t.on("fetch-start",y),t.on("fn-start",m),t.on("fetch-done",w)}(e,this.ee,this.handler,this.dt),this.importAggregator(e)}}function pe(e,t){var r=(0,ie.D)(t),n=e.params||e;n.hostname=r.hostname,n.port=r.port,n.protocol=r.protocol,n.host=r.hostname+":"+r.port,n.pathname=r.pathname,e.parsedOrigin=r,e.sameOrigin=r.sameOrigin}const ge={},me=["pushState","replaceState"];function ve(e){const t=function(e){return(e||B.ee).get("history")}(e);return!p.RI||ge[t.debugId]++||(ge[t.debugId]=1,(0,W.YM)(t).inPlace(window.history,me,"-")),t}var be=i(3738);const{He:ye,bD:we,d3:Re,Kp:xe,TZ:Ee,Lc:Ae,uP:Te,Rz:Ne}=be;class Se extends b{static featureName=Ee;constructor(e,t=!0){super(e,Ee,t);if(!(0,m.V)(this.agentIdentifier))return void this.deregisterDrain();const r=this.ee;let n;ve(r),this.eventsEE=(0,F.u)(r),this.eventsEE.on(Te,(function(e,t){this.bstStart=(0,N.t)()})),this.eventsEE.on(Ae,(function(e,t){(0,x.p)("bst",[e[0],t,this.bstStart,(0,N.t)()],void 0,a.K7.sessionTrace,r)})),r.on(Ne+Re,(function(e){this.time=(0,N.t)(),this.startPath=location.pathname+location.hash})),r.on(Ne+xe,(function(e){(0,x.p)("bstHist",[location.pathname+location.hash,this.startPath,this.time],void 0,a.K7.sessionTrace,r)}));try{n=new PerformanceObserver((e=>{const t=e.getEntries();(0,x.p)(ye,[t],void 0,a.K7.sessionTrace,r)})),n.observe({type:we,buffered:!0})}catch(e){}this.importAggregator(e,{resourceObserver:n})}}var _e=i(2614);class Oe extends b{static featureName=t.TZ;#i;#o;constructor(e,r=!0){let n;super(e,t.TZ,r),this.replayRunning=!1,this.#o=e;try{n=JSON.parse(localStorage.getItem("".concat(_e.H3,"_").concat(_e.uh)))}catch(e){}(0,g.SR)(e.agentIdentifier)&&this.ee.on(t.G4.RECORD,(()=>this.#a())),this.#s(n)?(this.#i=n?.sessionReplayMode,this.#c()):this.importAggregator(e),this.ee.on("err",(e=>{this.replayRunning&&(this.errorNoticed=!0,(0,x.p)(t.G4.ERROR_DURING_REPLAY,[e],void 0,this.featureName,this.ee))})),this.ee.on(t.G4.REPLAY_RUNNING,(e=>{this.replayRunning=e}))}#s(e){return e&&(e.sessionReplayMode===_e.g.FULL||e.sessionReplayMode===_e.g.ERROR)||(0,g.Aw)(this.agentIdentifier)}#u=!1;async#c(e){if(!this.#u){this.#u=!0;try{const{Recorder:t}=await Promise.all([i.e(478),i.e(249)]).then(i.bind(i,8589));this.recorder??=new t({mode:this.#i,agentIdentifier:this.agentIdentifier,trigger:e,ee:this.ee,agentRef:this.#o}),this.recorder.startRecording(),this.abortHandler=this.recorder.stopRecording}catch(e){}this.importAggregator(this.#o,{recorder:this.recorder,errorNoticed:this.errorNoticed})}}#a(){this.featAggregate?this.featAggregate.mode!==_e.g.FULL&&this.featAggregate.initializeRecording(_e.g.FULL,!0):(this.#i=_e.g.FULL,this.#c(t.Qb.API),this.recorder&&this.recorder.parent.mode!==_e.g.FULL&&(this.recorder.parent.mode=_e.g.FULL,this.recorder.stopRecording(),this.recorder.startRecording(),this.abortHandler=this.recorder.stopRecording))}}var Ie=i(3962);class Pe extends b{static featureName=Ie.TZ;constructor(e,t=!0){if(super(e,Ie.TZ,t),!p.RI||!(0,R.dV)().o.MO)return;const r=ve(this.ee);Ie.tC.forEach((e=>{(0,A.sp)(e,(e=>{a(e)}),!0)}));const n=()=>(0,x.p)("newURL",[(0,N.t)(),""+window.location],void 0,this.featureName,this.ee);r.on("pushState-end",n),r.on("replaceState-end",n);try{this.removeOnAbort=new AbortController}catch(e){}(0,A.sp)("popstate",(e=>(0,x.p)("newURL",[e.timeStamp,""+window.location],void 0,this.featureName,this.ee)),!0,this.removeOnAbort?.signal);let i=!1;const o=new((0,R.dV)().o.MO)(((e,t)=>{i||(i=!0,requestAnimationFrame((()=>{(0,x.p)("newDom",[(0,N.t)()],void 0,this.featureName,this.ee),i=!1})))})),a=(0,v.s)((e=>{(0,x.p)("newUIEvent",[e],void 0,this.featureName,this.ee),o.observe(document.body,{attributes:!0,childList:!0,subtree:!0,characterData:!0})}),100,{leading:!0});this.abortHandler=function(){this.removeOnAbort?.abort(),o.disconnect(),this.abortHandler=void 0},this.importAggregator(e,{domObserver:o})}}var je=i(7378);const Ce={},ke=["appendChild","insertBefore","replaceChild"];function Le(e){const t=function(e){return(e||B.ee).get("jsonp")}(e);if(!p.RI||Ce[t.debugId])return t;Ce[t.debugId]=!0;var r=(0,W.YM)(t),n=/[?&](?:callback|cb)=([^&#]+)/,i=/(.*)\.([^.]+)/,o=/^(\w+)(\.|$)(.*)$/;function a(e,t){if(!e)return t;const r=e.match(o),n=r[1];return a(r[3],t[n])}return r.inPlace(Node.prototype,ke,"dom-"),t.on("dom-start",(function(e){!function(e){if(!e||"string"!=typeof e.nodeName||"script"!==e.nodeName.toLowerCase())return;if("function"!=typeof e.addEventListener)return;var o=(s=e.src,c=s.match(n),c?c[1]:null);var s,c;if(!o)return;var u=function(e){var t=e.match(i);if(t&&t.length>=3)return{key:t[2],parent:a(t[1],window)};return{key:e,parent:window}}(o);if("function"!=typeof u.parent[u.key])return;var d={};function l(){t.emit("jsonp-end",[],d),e.removeEventListener("load",l,(0,A.jT)(!1)),e.removeEventListener("error",f,(0,A.jT)(!1))}function f(){t.emit("jsonp-error",[],d),t.emit("jsonp-end",[],d),e.removeEventListener("load",l,(0,A.jT)(!1)),e.removeEventListener("error",f,(0,A.jT)(!1))}r.inPlace(u.parent,[u.key],"cb-",d),e.addEventListener("load",l,(0,A.jT)(!1)),e.addEventListener("error",f,(0,A.jT)(!1)),t.emit("new-jsonp",[e.src],d)}(e[0])})),t}const He={};function Me(e){const t=function(e){return(e||B.ee).get("promise")}(e);if(He[t.debugId])return t;He[t.debugId]=!0;var r=t.context,n=(0,W.YM)(t),i=p.gm.Promise;return i&&function(){function e(r){var o=t.context(),a=n(r,"executor-",o,null,!1);const s=Reflect.construct(i,[a],e);return t.context(s).getCtx=function(){return o},s}p.gm.Promise=e,Object.defineProperty(e,"name",{value:"Promise"}),e.toString=function(){return i.toString()},Object.setPrototypeOf(e,i),["all","race"].forEach((function(r){const n=i[r];e[r]=function(e){let i=!1;[...e||[]].forEach((e=>{this.resolve(e).then(a("all"===r),a(!1))}));const o=n.apply(this,arguments);return o;function a(e){return function(){t.emit("propagate",[null,!i],o,!1,!1),i=i||!e}}}})),["resolve","reject"].forEach((function(r){const n=i[r];e[r]=function(e){const r=n.apply(this,arguments);return e!==r&&t.emit("propagate",[e,!0],r,!1,!1),r}})),e.prototype=i.prototype;const o=i.prototype.then;i.prototype.then=function(...e){var i=this,a=r(i);a.promise=i,e[0]=n(e[0],"cb-",a,null,!1),e[1]=n(e[1],"cb-",a,null,!1);const s=o.apply(this,e);return a.nextPromise=s,t.emit("propagate",[i,!0],s,!1,!1),s},i.prototype.then[W.Jt]=o,t.on("executor-start",(function(e){e[0]=n(e[0],"resolve-",this,null,!1),e[1]=n(e[1],"resolve-",this,null,!1)})),t.on("executor-err",(function(e,t,r){e[1](r)})),t.on("cb-end",(function(e,r,n){t.emit("propagate",[n,!0],this.nextPromise,!1,!1)})),t.on("propagate",(function(e,r,n){this.getCtx&&!r||(this.getCtx=function(){if(e instanceof Promise)var r=t.context(e);return r&&r.getCtx?r.getCtx():this})}))}(),t}const De={},Ke="setTimeout",Ue="setInterval",Ve="clearTimeout",Ge="-start",Fe=[Ke,"setImmediate",Ue,Ve,"clearImmediate"];function Be(e){const t=function(e){return(e||B.ee).get("timer")}(e);if(De[t.debugId]++)return t;De[t.debugId]=1;var r=(0,W.YM)(t);return r.inPlace(p.gm,Fe.slice(0,2),Ke+"-"),r.inPlace(p.gm,Fe.slice(2,3),Ue+"-"),r.inPlace(p.gm,Fe.slice(3),Ve+"-"),t.on(Ue+Ge,(function(e,t,n){e[0]=r(e[0],"fn-",null,n)})),t.on(Ke+Ge,(function(e,t,n){this.method=n,this.timerDuration=isNaN(e[1])?0:+e[1],e[0]=r(e[0],"fn-",this,n)})),t}const We={};function ze(e){const t=function(e){return(e||B.ee).get("mutation")}(e);if(!p.RI||We[t.debugId])return t;We[t.debugId]=!0;var r=(0,W.YM)(t),n=p.gm.MutationObserver;return n&&(window.MutationObserver=function(e){return this instanceof n?new n(r(e,"fn-")):n.apply(this,arguments)},MutationObserver.prototype=n.prototype),t}const{TZ:qe,d3:Ze,Kp:Ye,$p:Je,wW:Xe,e5:$e,tH:Qe,uP:et,rw:tt,Lc:rt}=je;class nt extends b{static featureName=qe;constructor(e,t=!0){if(super(e,qe,t),!p.RI)return;try{this.removeOnAbort=new AbortController}catch(e){}let r,n=0;const i=this.ee.get("tracer"),o=Le(this.ee),a=Me(this.ee),s=Be(this.ee),c=Z(this.ee),u=this.ee.get("events"),d=ne(this.ee),l=ve(this.ee),f=ze(this.ee);function h(e,t){l.emit("newURL",[""+window.location,t])}function g(){n++,r=window.location.hash,this[et]=(0,N.t)()}function m(){n--,window.location.hash!==r&&h(0,!0);var e=(0,N.t)();this[$e]=~~this[$e]+e-this[et],this[rt]=e}function v(e,t){e.on(t,(function(){this[t]=(0,N.t)()}))}this.ee.on(et,g),a.on(tt,g),o.on(tt,g),this.ee.on(rt,m),a.on(Xe,m),o.on(Xe,m),this.ee.on("fn-err",((...t)=>{t[2]?.__newrelic?.[e.agentIdentifier]||(0,x.p)("function-err",[...t],void 0,this.featureName,this.ee)})),this.ee.buffer([et,rt,"xhr-resolved"],this.featureName),u.buffer([et],this.featureName),s.buffer(["setTimeout"+Ye,"clearTimeout"+Ze,et],this.featureName),c.buffer([et,"new-xhr","send-xhr"+Ze],this.featureName),d.buffer([Qe+Ze,Qe+"-done",Qe+Je+Ze,Qe+Je+Ye],this.featureName),l.buffer(["newURL"],this.featureName),f.buffer([et],this.featureName),a.buffer(["propagate",tt,Xe,"executor-err","resolve"+Ze],this.featureName),i.buffer([et,"no-"+et],this.featureName),o.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"],this.featureName),v(d,Qe+Ze),v(d,Qe+"-done"),v(o,"new-jsonp"),v(o,"jsonp-end"),v(o,"cb-start"),l.on("pushState-end",h),l.on("replaceState-end",h),window.addEventListener("hashchange",h,(0,A.jT)(!0,this.removeOnAbort?.signal)),window.addEventListener("load",h,(0,A.jT)(!0,this.removeOnAbort?.signal)),window.addEventListener("popstate",(function(){h(0,n>1)}),(0,A.jT)(!0,this.removeOnAbort?.signal)),this.abortHandler=this.#n,this.importAggregator(e)}#n(){this.removeOnAbort?.abort(),this.abortHandler=void 0}}var it=i(3333);class ot extends b{static featureName=it.TZ;constructor(e,t=!0){super(e,it.TZ,t);const r=[e.init.page_action.enabled,e.init.performance.capture_marks,e.init.performance.capture_measures,e.init.user_actions.enabled,e.init.performance.resources.enabled];if(p.RI&&(e.init.user_actions.enabled&&(it.Zp.forEach((e=>(0,A.sp)(e,(e=>(0,x.p)("ua",[e],void 0,this.featureName,this.ee)),!0))),it.qN.forEach((e=>{const t=(0,v.s)((e=>{(0,x.p)("ua",[e],void 0,this.featureName,this.ee)}),500,{leading:!0});(0,A.sp)(e,t)}))),e.init.performance.resources.enabled&&p.gm.PerformanceObserver?.supportedEntryTypes.includes("resource"))){new PerformanceObserver((e=>{e.getEntries().forEach((e=>{(0,x.p)("browserPerformance.resource",[e],void 0,this.featureName,this.ee)}))})).observe({type:"resource",buffered:!0})}r.some((e=>e))?this.importAggregator(e):this.deregisterDrain()}}var at=i(993),st=i(3785),ct=i(9414);class ut extends b{static featureName=at.TZ;constructor(e,t=!0){super(e,at.TZ,t);const r=this.ee;(0,ct.J)(r,p.gm.console,"log",{level:"info"}),(0,ct.J)(r,p.gm.console,"error",{level:"error"}),(0,ct.J)(r,p.gm.console,"warn",{level:"warn"}),(0,ct.J)(r,p.gm.console,"info",{level:"info"}),(0,ct.J)(r,p.gm.console,"debug",{level:"debug"}),(0,ct.J)(r,p.gm.console,"trace",{level:"trace"}),this.ee.on("wrap-logger-end",(function([e]){const{level:t,customAttributes:n}=this;(0,st.R)(r,e,n,t)})),this.importAggregator(e)}}new class extends o{constructor(t){super(),p.gm?(this.features={},(0,R.bQ)(this.agentIdentifier,this),this.desiredFeatures=new Set(t.features||[]),this.desiredFeatures.add(w),this.runSoftNavOverSpa=[...this.desiredFeatures].some((e=>e.featureName===a.K7.softNav)),(0,d.j)(this,t,t.loaderType||"agent"),this.run()):(0,e.R)(21)}get config(){return{info:this.info,init:this.init,loader_config:this.loader_config,runtime:this.runtime}}run(){try{const t=u(this.agentIdentifier),r=[...this.desiredFeatures];r.sort(((e,t)=>a.P3[e.featureName]-a.P3[t.featureName])),r.forEach((r=>{if(!t[r.featureName]&&r.featureName!==a.K7.pageViewEvent)return;if(this.runSoftNavOverSpa&&r.featureName===a.K7.spa)return;if(!this.runSoftNavOverSpa&&r.featureName===a.K7.softNav)return;const n=function(e){switch(e){case a.K7.ajax:return[a.K7.jserrors];case a.K7.sessionTrace:return[a.K7.ajax,a.K7.pageViewEvent];case a.K7.sessionReplay:return[a.K7.sessionTrace];case a.K7.pageViewTiming:return[a.K7.pageViewEvent];default:return[]}}(r.featureName).filter((e=>!(e in this.features)));n.length>0&&(0,e.R)(36,{targetFeature:r.featureName,missingDependencies:n}),this.features[r.featureName]=new r(this)}))}catch(t){(0,e.R)(22,t);for(const e in this.features)this.features[e].abortHandler?.();const r=(0,R.Zm)();delete r.initializedAgents[this.agentIdentifier]?.api,delete r.initializedAgents[this.agentIdentifier]?.features,delete this.sharedAggregator;return r.ee.get(this.agentIdentifier).abort(),!1}}}({features:[he,w,S,Se,Oe,O,M,ot,ut,Pe,nt],loaderType:"spa"})})()})();</script>
# 	<meta name="author" content="School of Public and Population Health">

# 		<meta name="HandheldFriendly" content="True">
# 	<meta name="viewport" content="width=device-width, initial-scale=1.0">

# 		<meta name="apple-mobile-web-app-title" content="Faculty and Staff Directory">

# 		<meta name="application-name" content="School of Public and Population Health">

# 	<link rel="stylesheet" type="text/css" href="https://cloud.typography.com/6665036/7251792/css/fonts.css" />

	
#         <script type="text/javascript">
#             function is_browser() {
#                 return (
#                     navigator.userAgent.indexOf("Chrome") !== - 1 ||
#                     navigator.userAgent.indexOf("Opera") !== - 1 ||
#                     navigator.userAgent.indexOf("Firefox") !== - 1 ||
#                     navigator.userAgent.indexOf("MSIE") !== - 1 ||
#                     navigator.userAgent.indexOf("Safari") !== - 1 ||
#                     navigator.userAgent.indexOf("Edge") !== - 1
#                 );
#             }

#             function less_than_ie9() {
# 				return !document.addEventListener;
#             }

#             function not_excluded_page() {
#                 return (
#                     window.location.href.indexOf("/unsupported-browser/") === - 1 &&
#                     document.title.toLowerCase().indexOf('page not found') === - 1
#                 );
#             }

#             if (is_browser() && less_than_ie9() && not_excluded_page()) {
#                 window.location = location.protocol + '//' + location.host + '/unsupported-browser/';
#             }
#         </script>

# 		<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
# 	<style>img:is([sizes="auto" i], [sizes^="auto," i]) { contain-intrinsic-size: 3000px 1500px }</style>
	
# 	<!-- This site is optimized with the Yoast SEO Premium plugin v24.4 (Yoast SEO v24.4) - https://yoast.com/wordpress/plugins/seo/ -->
# 	<title>Faculty and Staff Directory - School of Public and Population Health</title>
# 	<link rel="canonical" href="https://www.boisestate.edu/spph/faculty-and-staff-directory/" />
# 	<meta property="og:locale" content="en_US" />
# 	<meta property="og:type" content="article" />
# 	<meta property="og:title" content="Faculty and Staff Directory" />
# 	<meta property="og:description" content="Faculty &amp; Staff Online Forms" />
# 	<meta property="og:url" content="https://www.boisestate.edu/spph/faculty-and-staff-directory/" />
# 	<meta property="og:site_name" content="School of Public and Population Health" />
# 	<meta property="article:modified_time" content="2025-02-19T17:20:29+00:00" />
# 	<meta name="twitter:card" content="summary_large_image" />
# 	<meta name="twitter:label1" content="Est. reading time" />
# 	<meta name="twitter:data1" content="4 minutes" />
# 	<!-- / Yoast SEO Premium plugin. -->


# <link rel='dns-prefetch' href='//www.boisestate.edu' />
# <link rel='dns-prefetch' href='//customer.cludo.com' />
# <link rel='stylesheet' id='openid_admin_settings_style-css' href='https://www.boisestate.edu/spph/wp-content/plugins/openid-connect-sso/includes/css/openid_style.css?version=2.0&#038;ver=6.7.2' type='text/css' media='all' />
# <link rel='stylesheet' id='wp-block-library-css' href='https://www.boisestate.edu/spph/wp-includes/css/dist/block-library/style.min.css?ver=6.7.2' type='text/css' media='all' />
# <style id='global-styles-inline-css' type='text/css'>
# :root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:root { --wp--style--global--content-size: 754px;--wp--style--global--wide-size: 1192px; }:where(body) { margin: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}a:where(:not(.wp-element-button)){text-decoration: underline;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;line-height: inherit;padding: calc(0.667em + 2px) calc(1.333em + 2px);text-decoration: none;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
# :where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
# :where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
# :root :where(.wp-block-pullquote){font-size: 1.5em;line-height: 1.6;}
# </style>
# <link rel='stylesheet' id='core-theme-base-css' href='https://www.boisestate.edu/spph/wp-content/themes/core/css/dist/master.min.css?ver=1.16.02.06.2025' type='text/css' media='all' />
# <link rel='stylesheet' id='core-theme-print-css' href='https://www.boisestate.edu/spph/wp-content/themes/core/css/dist/print.min.css?ver=1.16.02.06.2025' type='text/css' media='print' />
# <link rel='stylesheet' id='multisite-json-api-plugin-styles-css' href='https://www.boisestate.edu/spph/wp-content/plugins/multisite-json-api-master/public/assets/css/public.css?ver=1.0.0' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-default-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/css/build/default.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-datatables-buttons-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/datatables.buttons.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-datatables-columnfilterwidgets-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/datatables.columnfilterwidgets.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-datatables-fixedheader-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/datatables.fixedheader.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-datatables-fixedcolumns-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/datatables.fixedcolumns.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-datatables-scroll-buttons-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/datatables.scroll-buttons.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-datatables-serverside-processing-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/datatables.serverside-processing.css?ver=3.0.3' type='text/css' media='all' />
# <link rel='stylesheet' id='tablepress-responsive-tables-css' href='https://www.boisestate.edu/spph/wp-content/plugins/tablepress-premium/modules/css/build/responsive-tables.css?ver=3.0.3' type='text/css' media='all' />
# <script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/themes/core/js/vendor/jquery.min.js?ver=1.16.02.06.2025" id="jquery-js"></script>
# <script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/plugins/multisite-json-api-master/public/assets/js/public.js?ver=1.0.0" id="multisite-json-api-plugin-script-js"></script>
# <link rel="https://api.w.org/" href="https://www.boisestate.edu/spph/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://www.boisestate.edu/spph/wp-json/wp/v2/pages/22420" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.boisestate.edu/spph/xmlrpc.php?rsd" />
# <meta name="generator" content="WordPress 6.7.2" />
# <link rel='shortlink' href='https://www.boisestate.edu/spph/?p=22420' />
# <link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://www.boisestate.edu/spph/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.boisestate.edu%2Fspph%2Ffaculty-and-staff-directory%2F" />
# <link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://www.boisestate.edu/spph/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.boisestate.edu%2Fspph%2Ffaculty-and-staff-directory%2F&#038;format=xml" />

# 		   <!-- Google Tag Manager -->
# 		   <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
# 		   new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
# 		   j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
# 		   'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
# 		   })(window,document,'script','dataLayer','GTM-5N3ZK6J');</script>
# 		   <!-- End Google Tag Manager -->

#    		<link rel="shortcut icon" href="https://www.boisestate.edu/spph/wp-content/themes/core/img/theme/branding-assets/favicon.ico"><link rel="icon" sizes="192x192" href="https://www.boisestate.edu/spph/wp-content/themes/core/img/theme/branding-assets/android-icon.png"><link rel="apple-touch-icon-precomposed" href="https://www.boisestate.edu/spph/wp-content/themes/core/img/theme/branding-assets/apple-touch-icon-precomposed.png"><meta name="msapplication-TileImage" content="https://www.boisestate.edu/spph/wp-content/themes/core/img/theme/branding-assets/ms-icon-144.png"><meta name="msapplication-TileColor" content="#ffffff"><meta name="theme-color" content="#ffffff">

# </head>

# <body class="page-template-default page page-id-22420 page-parent has-panels has-page-content page-faculty-and-staff-directory" data-js="site-wrap">

	
# 		<!-- Google Tag Manager (noscript) -->
# 		<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5N3ZK6J"
# 		height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
# 		<!-- End Google Tag Manager (noscript) -->

		

	
	
# 	<a href="#a11y-skip-link-content" class="a11y-skip-link u-visual-hide">Skip to main content</a>

# 			<header class="site-header" data-js="site-header">

#     <div class="site-header__wrapper">

#         <div class="site-header__wrapper-inner">

#             <div class="site-header__brand" data-js="site-header-brand">

#                 <div class="logo" data-js="logo">
# 				<a href="https://www.boisestate.edu/" class="logo__wrap svgicon" rel="home">
# 					<span class="u-visual-hide">School of Public and Population Health Home</span>
# 				</a>
# 			</div>

#                 <div
#                         class="site-header__search-mobile"
#                         data-js="site-search-mobile"
#                         aria-label="Site Search Mobile"
# 						id="cludo-search-form-mobile"
#                 >
                    
# <form class="c-search" role='search' method='get' aria-label='search-mobile'>

# 	<label class="c-search__label u-visual-hide" for='s-mobile'>Search</label>
# 	<input class="c-search__input" type='text' id='s-mobile' name='s-mobile' placeholder='Search' value='' data-js='search-box' autocomplete='off' />
	
# <button class=" site-header-trigger site-header-trigger--search-mobile icon icon-search-thick"
# 		type="submit"
# 				name='submit' aria-label='Site Search Toggle' data-js='search-submit'>
# 	</button>


# </form>

#                 </div>

#                 <button
#                         id="site-nav-mobile"
#                         class="site-header-trigger site-header-trigger--menu site-header-trigger--menu-mobile"
#                         data-js="site-nav-trigger-mobile"
#                         data-id="site-nav-mobile"
#                         aria-label="Site Navigation Toggle"
#                         aria-expanded="false"
#                 >
# 					<span class="site-header-trigger__wrapper">
# 						<i
#                                 class="site-header-trigger__icon site-header-trigger__icon--menu icon icon-menu"
#                                 aria-hidden="true"
#                                 title="Open"
#                         ></i>
# 						<i
#                                 class="site-header-trigger__icon site-header-trigger__icon--menu-close icon icon-menu-close"
#                                 aria-hidden="true"
#                                 title="Close"
#                         ></i>
#                         <span class="u-visual-hide">Menu</span>
# 					</span>
#                 </button>

#             </div>

#         </div>

#             <nav class="site-nav-primary" data-js="" aria-labelledby="site-header__primary-nav-label">

#         <h2 id="site-header__primary-nav-label" class="u-visual-hide">Boise Global Navigation</h2>

#         <ol class="site-nav-primary__list">
#             <li class="primary__list-item primary__list-item--depth-0"><a href="https://www.boisestate.edu/admissions/apply/" id="menu-item-1253" class="site-nav__action primary__action primary__action--depth-0">Apply</a></li>
# <li class="primary__list-item primary__list-item--depth-0"><a href="https://www.boisestate.edu/admissions/visit/" id="menu-item-1252" class="site-nav__action primary__action primary__action--depth-0">Visit</a></li>
# <li class="primary__list-item primary__list-item--depth-0"><a href="https://www.boisestate.edu/giving/" id="menu-item-1988" class="site-nav__action primary__action primary__action--depth-0">Give</a></li>


#             <li class="primary__list-item primary__list-item--desktop primary__list-item--depth-0">
#                 <button
#                         id="site-nav-desktop-trigger"
#                         class="site-header-trigger site-header-trigger--menu site-header-trigger--menu-full"
#                         data-js="site-nav-menu-trigger"
#                         data-id="site-nav-desktop-off-canvas"
#                         aria-label="Desktop Menu Toggle"
#                         aria-expanded="false"
#                 >
# 				<span class="site-header-trigger__wrapper">
#                     <span class="site-header-trigger__label">Menu</span>
# 					<i
#                             class="site-header-trigger__icon site-header-trigger__icon--menu icon icon-menu"
#                             aria-hidden="true"
#                             title="Open"
#                     ></i>
# 					<i
#                             class="site-header-trigger__icon site-header-trigger__icon--menu-close icon icon-menu-close"
#                             aria-hidden="true"
#                             title="Close"
#                     ></i>
# 				</span>
#                 </button>
#                 <nav
#                         id="site-nav-desktop-off-canvas-menu"
#                         class="site-nav__menu site-nav__menu--desktop-off-canvas"
#                         data-js="site-nav-menu"
#                         data-id="site-nav-desktop-off-canvas"
#                         aria-hidden="true"
#                         aria-label="Boise Main Menu"
#                 >
#                     <div class="site-nav__menu-wrapper-outer">
#                         <div class="site-nav__menu-wrapper">
#                             <section class="site-nav__menu-child-wrapper" data-js="site-nav-desktop-off-canvas-menu-wrapper" aria-label="Site Navigation">
#                                 <div class="site-nav__menu-cta">
# 	                                                                        <span> Ready to take the next step? <a href="https://www.boisestate.edu/admissions/virtual-visits/" class="site-nav-menu-tagline-action" data-js="site-nav-menu-action" rel="noopener">Plan your virtual visit. <i class="icon icon-long-arrow-right"></i></a></span>
# 	                                                                </div>
#                             </section>
#                         </div>
#                     </div>
#                 </nav>
#             </li>

#             <li class="primary__list-item primary__list-item--search primary__list-item--depth-0">
#                 <button
#                         id="site-search-trigger-full"
#                         class="site-header-trigger site-header-trigger--search site-header-trigger--search-full site-nav-full__item site-nav-full__item--search"
#                         data-js="site-search-trigger-desktop"
#                         aria-label="Site Search Toggle"
#                         aria-expanded="false"
#                 >
#                     <span class="site-header-trigger__label">Search</span>
#                     <i
#                             class="site-header-trigger__icon site-header-trigger__icon--search icon icon-search-thick"
#                             aria-hidden="true"
#                             title="Open"
#                     ></i>
#                     <i
#                             class="site-header-trigger__icon site-header-trigger__icon--search-close icon icon-menu-close"
#                             aria-hidden="true"
#                             title="Close"
#                     ></i>
#                 </button>
#             </li>
#         </ol>

#     </nav>

#     		<script>/* eslint-disable */
# var modernTribe = window.modernTribe || {};
# (function(mt) {
# 	var header = mt.headerRender = mt.headerRender || {};
# 	var forEach = Function.prototype.call.bind(Array.prototype.forEach);

# 	header.util = {
# 		debounce: function(func, wait, immediate) {
# 			var timeout;
# 			return function() {
# 				var context = this, args = arguments;
# 				var later = function() {
# 					timeout = null;
# 					if (!immediate) func.apply(context, args);
# 				};
# 				var callNow = immediate && !timeout;
# 				clearTimeout(timeout);
# 				timeout = setTimeout(later, wait);
# 				if (callNow) func.apply(context, args);
# 			};
# 		},

# 		trigger: function(el, eventName, data) {
# 			var event;
# 			try {
# 				event = new CustomEvent(eventName, { detail: data });
# 			} catch (e) {
# 				event = document.createEvent('CustomEvent');
# 				event.initCustomEvent(eventName, true, true, data);
# 			}

# 			el.dispatchEvent(event);
# 		}
# 	};

# 	header.primary = {
# 		mobileBreakpoint: 768,
# 		el: document.getElementsByClassName('site-nav-primary')[0],
# 		wrapper: document.getElementsByClassName('site-header')[0],
# 		viewport: document.documentElement.clientWidth,

# 		state: {
# 			firstRun: true,
# 			isDesktop: false,
# 		},

# 		isMobile: function() {
# 			return document.documentElement.clientWidth < this.mobileBreakpoint;
# 		},

# 		bindEvents: function() {
# 			window.addEventListener('resize', header.util.debounce(this.handleResize, 25));
# 			document.addEventListener('modern_tribe/fonts_loaded', this.handleResize);
# 		},

# 		toggleBodyClass: function() {
# 			var _this = this;
# 			document.body.classList.remove('site-header--mobile-active');

# 			if (!this.state.isDesktop) {
# 				document.body.classList.remove('site-header--desktop-active');
# 				forEach(this.el.querySelectorAll('.primary__list-item--dynamic'), function(node) {
# 					_this.el.querySelector('.site-nav__list--primary').appendChild(node);
# 				});
# 			} else {
# 				document.body.classList.add('site-header--desktop-active');
# 				forEach(this.el.querySelector('.site-nav__list--primary').querySelectorAll('.primary__list-item--dynamic'), function(node) {
# 					_this.el.querySelector('.site-nav-primary__list').insertBefore(node, _this.el.querySelector('.primary__list-item--guide'));
# 				});
# 			}
# 		},

# 		handleResize: function() {
# 			if (document.documentElement.clientWidth >= header.primary.mobileBreakpoint) {
# 				header.primary.toggleBodyClass();
# 			} else {
# 				header.primary.state.isDesktop = false;
# 				document.body.classList.add('site-header--mobile-active');
# 				document.body.classList.remove('site-header--desktop-active');
# 			}

# 			header.primary.viewport = document.documentElement.clientWidth;
# 			header.util.trigger(document, 'modern_tribe/nav_resized');
# 		},

# 		init: function () {
# 			if (!this.el) {
# 				return;
# 			}

# 			if (this.isMobile()) {
# 				document.body.classList.add('site-header--mobile-active');
# 				document.body.classList.remove('site-header--desktop-active');
# 			} else {
# 				this.toggleBodyClass();
# 			}

# 			this.bindEvents();
# 		}
# 	};

# 	header.primary.init();
# })(modernTribe);
# </script>
		


#     </div>

# <div id="site-header-search" class="site-header__search" data-js="site-search-global" aria-hidden="true" data-search-path="/spph/">
#     <div class="site-header__search-wrapper-outer">
#         <div class="site-header__search-wrapper-inner" id="cludo-search-form">
	        
# <form class="c-search" role='search' method='get' aria-label='search-desktop'>

# 	<label class="c-search__label u-visual-hide" for='s-desktop'>Search</label>
# 	<input class="c-search__input" type='text' id='s-desktop' name='s-desktop' placeholder='Search' value='' data-js='search-box' autocomplete='off' />
	
# <button class=" site-header-trigger site-header-trigger--search-mobile icon icon-search-thick"
# 		type="submit"
# 				name='submit' aria-label='Site Search Toggle' data-js='search-submit'>
# 	</button>


# </form>

# 			<div class="search-toggle" data-js="search-toggle">
# 	<div tabindex="0" class="search-toggle__all search-toggle-container">
# 		<input tabindex="-1" type="radio" class="all-boise" title="All Boise" id="all-boise1" name="site1" value="all" checked>
# 		<label for="all-boise1">
# 			All Boise State
# 		</label>
# 	</div>

# 	<div tabindex="0" class="search-toggle__section search-toggle-container">
# 		<input tabindex="-1" type="radio" class="this-section" title="This Section Only" id="this-section1" name="site1" value="https://www.boisestate.edu/spph">
# 		<label for="this-section1">

# 			School of Public and Population Health Only
# 		</label>
# 	</div>
# </div>
#         </div>
#     </div>
# </div>


# </header>

	
# 				<nav class="nav-section__secondary" data-js="secondary-nav" aria-label="Section Navigation">
# 		<div class="nav-section__secondary-contain">
# 			<ul class="nav-section__secondary-list">
# 				<li class="main__list-item nav-section__title">
# 					<h2>
# 						<a href="https://www.boisestate.edu/spph" class="nav-section__title-wrapper">
# 							School of Public and Population Health
# 						</a>
# 					</h2>
# 				</li>
# 				<li class="main__list-item main__list-item--depth-0 main__list-item--has-children"><a href="https://www.boisestate.edu/spph/undergraduate/" class="site-nav__action main__action main__action--depth-0 main__action--has-children">Undergraduate Degrees</a></li><li class="main__list-item main__list-item--depth-0 main__list-item--has-children"><a href="https://www.boisestate.edu/spph/mph/" class="site-nav__action main__action main__action--depth-0 main__action--has-children">Master of Public Health</a></li><li class="main__list-item main__list-item--depth-0 main__list-item--has-children"><a href="https://www.boisestate.edu/spph/phd/" class="site-nav__action main__action main__action--depth-0 main__action--has-children">PhD in Public and Population Health Leadership</a></li><li class="main__list-item main__list-item--depth-0"><a href="https://www.boisestate.edu/spph/about-spph/" class="site-nav__action main__action main__action--depth-0">About SPPH</a></li><li class="main__list-item main__list-item--depth-0 main__list-item--is-current"><a href="https://www.boisestate.edu/spph/faculty-and-staff-directory/" aria-current="page" class="site-nav__action main__action main__action--depth-0">Faculty and Staff</a></li><li class="main__list-item main__list-item--depth-0"><a href="https://www.boisestate.edu/spph/map-directions/" class="site-nav__action main__action main__action--depth-0">Contact SPPH</a></li><li class="main__list-item main__list-item--depth-0 main__list-item--has-children"><a href="https://www.boisestate.edu/spph/resources/" class="site-nav__action main__action main__action--depth-0 main__action--has-children">Student Resources</a></li><li class="main__list-item main__list-item--depth-0 main__list-item--has-children"><a href="https://www.boisestate.edu/spph/spph-projects-and-initiatives/" class="site-nav__action main__action main__action--depth-0 main__action--has-children">SPPH Projects and Initiatives</a></li><li class="main__list-item main__list-item--depth-0"><a href="https://www.boisestate.edu/spph/alumni-and-giving/" class="site-nav__action main__action main__action--depth-0">Alumni and Giving</a></li>
# 			</ul>
# 			<div class="nav-section__secondary-item nav-section__secondary-item--trigger">
# 				<button
# 						id="nav-section-more-trigger"
# 						class="nav-section__trigger"
# 						data-js="nav-section-more-trigger"
# 						aria-label="More Site Navigation Toggle"
# 						aria-expanded="false"
# 				>
# 					<span class="nav-section__trigger-text">
# 						<i class="nav-section__trigger-icon icon icon-dots" aria-hidden="true"></i>
# 						More
# 						<span class="u-visual-hide">section menu items</span>
# 					</span>
# 				</button>
# 				<div
# 					class="nav-section__menu"
# 					data-js="nav-section-menu"
# 					aria-hidden="true"
# 					aria-labelledby="nav-section-more-trigger"
# 				>
# 					<div class="nav-section__menu-wrapper">
# 						<ul
# 							id="nav-section-menu"
# 							class="nav-section__menu-wrapper-inner"
# 						>
# 						</ul>
# 					</div>
# 				</div>
# 			</div>
# 		</div>
# 	</nav>

	
# 			<script>/* eslint-disable */
# var modernTribe = window.modernTribe || {};
# (function(mt) {
# 	var secondaryNav = mt.secondaryNavRender = mt.secondaryNavRender || {};
# 	var forEach = Function.prototype.call.bind(Array.prototype.forEach);

# 	secondaryNav.util = {
# 		trigger: function(el, eventName, data) {
# 			var event;
# 			try {
# 				event = new CustomEvent(eventName, { detail: data });
# 			} catch (e) {
# 				event = document.createEvent('CustomEvent');
# 				event.initCustomEvent(eventName, true, true, data);
# 			}

# 			el.dispatchEvent(event);
# 		}
# 	};

# 	secondaryNav.primary = {
# 		el: document.getElementsByClassName('nav-section__secondary')[0],
# 		wrapper: document.getElementsByClassName('nav-section__secondary-list')[0],
# 		menuChild: document.getElementById('nav-section-menu'),
# 		trigger: document.getElementsByClassName('nav-section__secondary-list-item--trigger')[0],
# 		viewport: document.documentElement.clientWidth,
# 		subhead: document.getElementById('site-subhead'),

# 		bindEvents: function() {
# 			var _this = this;
# 			window.addEventListener('resize', this.handleResize);
# 			document.addEventListener('modern_tribe/fonts_loaded', this.handleResize);
# 			setTimeout(function() {
# 				_this.handleResize();
# 			}, 300);
# 		},

# 		reorganize: function() {
# 			var _this = this;
			
# 			const rChildren = _this.menuChild.children;
# 			let numW = 0;

# 			[...rChildren].forEach(item => {
# 				item.outHTML = '';
# 				_this.wrapper.appendChild(item);
# 			})

# 			const teleW = _this.wrapper.offsetWidth,
# 				tChildren = _this.wrapper.children;

# 			[...tChildren].forEach(item => {
# 				numW += item.getBoundingClientRect().width;

# 				if (numW > teleW) {
# 				item.outHTML = '';
# 				_this.menuChild.appendChild(item);
# 				}
# 			});

# 			_this.switchState();
# 		},

# 		switchState: function() {
# 			if (this.menuChild.querySelectorAll('.main__list-item').length && document.body.classList.contains('site-secondary-nav--active')) {
# 				return;
# 			} else if (this.menuChild.querySelectorAll('.main__list-item').length && !document.body.classList.contains('site-secondary-nav--active')) {
# 				document.body.classList.add('site-secondary-nav--active');
# 			} else if (!this.menuChild.querySelectorAll('.main__list-item').length && document.body.classList.contains('site-secondary-nav--active')) {
# 				document.body.classList.remove('site-secondary-nav--active');
# 			}
# 		},

# 		loadClasses: function() {
# 			document.body.classList.add('page--has-secondary-nav');

# 			if (secondaryNav.primary.subhead) {
# 				document.body.classList.add('page--has-subhead');
# 			}
# 		},

# 		handleResize: function() {
# 			secondaryNav.primary.reorganize();

# 			secondaryNav.primary.viewport = document.documentElement.clientWidth;
# 			secondaryNav.util.trigger(document, 'modern_tribe/nav_resized');
# 		},

# 		init: function () {
# 			if (!this.el) {
# 				return;
# 			}

# 			this.loadClasses();
# 			this.bindEvents();
# 			this.reorganize();
# 		}
# 	};

# 	secondaryNav.primary.init();
# })(modernTribe);
# </script>
		

 
	

# <main>

# <div id="a11y-skip-link-content"></div>

# 		<div class="page-spacing">

# 		<div class="l-container l-container--inner">
												
# <div class="c-breadcrumbs__wrapper" >
# 	<ul class="c-breadcrumbs">

# 					<li class="c-breadcrumbs__item">
# 				<a href="https://www.boisestate.edu/spph" class="anchor c-breadcrumbs__anchor" >
# 					School of Public and Population Health
# 				</a>
# 			</li>
# 					<li class="c-breadcrumbs__item">
# 				<a href="https://www.boisestate.edu/spph/faculty-and-staff-directory/" class="anchor c-breadcrumbs__anchor" >
# 					Faculty and Staff Directory
# 				</a>
# 			</li>
# 			</ul>
# </div>
# 									</div>

		
# 			<div class="l-container l-container--inner">
# 				<div class="tertiary-header">
# 					<h1 class="h1">Faculty and Staff Directory</h1>
# 				</div>
# 			</div>

# 							<div class="wp-block-post-content">
	
# <p><a class="c-btn" href="https://www.boisestate.edu/spph/faculty-and-staff-online-request-forms/">Faculty &amp; Staff Online Forms</a></p>




# 			<div class="panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding"
# 				 data-index=""
# 				 data-js="panel"
# 				 data-type="people-list"
			     
# 				 data-modular-content>
	
# 	<div class="site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding">
# 	<div class="l-content--inner">
		
	
# 				<div class="oneUp">
# 				<header class="s-header t-content">
					
# <h2
# 		class="site-panel__title s-title h2"
# 		>

# 	Faculty

# </h2>
					
# 				</header>
# 			</div>
# 			<div class="s-content">
# 				<ul class="panel-people__listing oneUp">

# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Mike Mann headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Mike-Mann-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Mike Mann, PhD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	SPPH Director and Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: The intersection between public health and public schooling, academic achievement as a social determinant of health, student mental health promotion and school/community substance abuse prevention partnerships.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 112

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3334"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3334</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:mikemann@boisestate.edu"
# 			>
# 			<span class="c-btn__text">mikemann@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/mikemann/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Mike Mann</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: The intersection between public health and public schooling, academic achievement as a social determinant of health, student mental health promotion and school/community substance abuse prevention partnerships.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Mac McCullough headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2022/10/McCullough_Mac.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Mac McCullough, PhD, MPH

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Professor and Associate Director for Community Engagement and Impact

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p><span style="font-weight: 400">Areas of interest: Health finance, health policy including value-based care, public health economics, social determinants of health, health management, academic health departments, healthcare analytics and health IT.</span></p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 106

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3923"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3923</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:macmccullough@boisestate.edu"
# 			>
# 			<span class="c-btn__text">macmccullough@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/mac-mccullough-phd-mph/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Mac McCullough</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p><span style="font-weight: 400">Areas of interest: Health finance, health policy including value-based care, public health economics, social determinants of health, health management, academic health departments, healthcare analytics and health IT.</span></p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Jaime Sand headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Jaime-Sand-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Jaime Sand, EdD, RHIA, CCS, CAHIMS

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Professor and Associate Director for Student Engagement and Impact

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Online and undergraduate curriculum and instruction, health information education, interprofessional education, medical coding training and nontraditional student engagement</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 109

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5392"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5392</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:jaimesand@boisestate.edu"
# 			>
# 			<span class="c-btn__text">jaimesand@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/jsand/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Jaime Sand</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Online and undergraduate curriculum and instruction, health information education, interprofessional education, medical coding training and nontraditional student engagement</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Anne Abbott" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/08/IMG_7453-1-1152x1252.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Anne Abbott, PhD, MPP

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Health Communication, Public Health Policy, Program Planning and Evaluation, Violence Prevention, and Adolescent and Young Adult Health.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 113

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5061"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5061</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:anneabbott@boisestate.edu"
# 			>
# 			<span class="c-btn__text">anneabbott@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/anne-abbot-phd-mpp/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Anne Abbott</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Health Communication, Public Health Policy, Program Planning and Evaluation, Violence Prevention, and Adolescent and Young Adult Health.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Travis Armstrong" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2024/07/Armstrong_Travis-1152x1440.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Travis Armstrong, MPA, RT (R)

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Associate Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p><span style="font-weight: 400">Areas of Interest: Connecting students to programs and resources that support their academic and professional journeys, eight dimensions of wellness, allied health professions, healthcare delivery in rural and underserved areas, impact of public lands and outdoor recreation on public health and wellness.</span></p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 102

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5062"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5062</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:travisarmstrong@boisestate.edu"
# 			>
# 			<span class="c-btn__text">travisarmstrong@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/faculty-and-staff-directory/travis-armstrong-rtr/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Travis Armstrong</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p><span style="font-weight: 400">Areas of Interest: Connecting students to programs and resources that support their academic and professional journeys, eight dimensions of wellness, allied health professions, healthcare delivery in rural and underserved areas, impact of public lands and outdoor recreation on public health and wellness.</span></p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Ed Baker headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Ed-Baker-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Ed Baker, PhD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Professor 

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Healthcare policy, rural workforce planning, healthcare financing and performance improvement.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Yanke Family Research Park 903

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3118"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3118</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:ebaker@boisestate.edu"
# 			>
# 			<span class="c-btn__text">ebaker@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/e-baker/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Ed Baker</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Healthcare policy, rural workforce planning, healthcare financing and performance improvement.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Desmond Banks headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Desmond-Banks-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Desmond Banks, PhD, MPH

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Social determinants of health, health disparities, health equity, chronic disease and program evaluation.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5063"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5063</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:desmondbanks@boisestate.edu"
# 			>
# 			<span class="c-btn__text">desmondbanks@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/desmond-banks-phd-mph/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio For Desmond Banks</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Social determinants of health, health disparities, health equity, chronic disease and program evaluation.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Kruti Chaliawala" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2024/08/Headshot_3-1152x1728.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Kruti Chaliawala, PhD, MS, MA, CHES

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of Interest: Psychosocial determinants of health behaviors among adolescents and young adults, sexual health, mental health, international student health disparities and minority health.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 103

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3921"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3921</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:krutichaliawala@boisestate.edu"
# 			>
# 			<span class="c-btn__text">krutichaliawala@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/faculty-and-staff-directory/kruti-chaliawala-phd-ms-ma-ches/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Kruti Chaliawala</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of Interest: Psychosocial determinants of health behaviors among adolescents and young adults, sexual health, mental health, international student health disparities and minority health.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Cynthia Curl headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Cynthia-Curl-Headshot-2.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Cynthia Curl, PhD, MS

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Associate Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Measuring human exposures to agricultural chemicals and improving health and safety in agricultural workplaces and agricultural communities. Student intern and volunteer positions are available in the Curl Agricultural Health lab.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3924"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3924</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:cynthiacurl@boisestate.edu"
# 			>
# 			<span class="c-btn__text">cynthiacurl@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/ccurl/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Cynthia Curl</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Measuring human exposures to agricultural chemicals and improving health and safety in agricultural workplaces and agricultural communities. Student intern and volunteer positions are available in the Curl Agricultural Health lab.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2025/02/Priyanka-Dubey-1152x1440.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	 Priyanka Dubey, PhD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Sexual and reproductive health and menstrual health of gender diverse communities, maternal and child health, global health</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 121

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5064"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5064</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:priyankadubey@boisestate.edu"
# 			>
# 			<span class="c-btn__text">priyankadubey@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/faculty-and-staff-directory/priyanka-dubey-phd/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for  Priyanka Dubey</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Sexual and reproductive health and menstrual health of gender diverse communities, maternal and child health, global health</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Ashley Havlicak" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2024/01/0-e1715637604494.webp" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Ashley Havlicak, MPH

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Policy, environment and systems change, school and adolescent health, mental health, health equity, social influencers of health, project management, collective impact and collaboration.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 124

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2188"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2188</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:ashleyhavlicak@boisestate.edu"
# 			>
# 			<span class="c-btn__text">ashleyhavlicak@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/ashley-havlicak-mph/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Ashley Havlicak</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Policy, environment and systems change, school and adolescent health, mental health, health equity, social influencers of health, project management, collective impact and collaboration.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2025/02/unnamed.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Andrea Hill, MPH, RD, LD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Assistant Teaching Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Community engagement strategies, youth mental health and well-being, public health nutrition issues, and the social determinants of health.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 124

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:andreahill565@boisestate.edu"
# 			>
# 			<span class="c-btn__text">andreahill565@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/andrea-hill-mph-rd-ld/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Andrea Hill</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Community engagement strategies, youth mental health and well-being, public health nutrition issues, and the social determinants of health.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Andy Hyer" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Andy-Hyer-Headshot-2.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Andy Hyer, JD, MHS

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Associate Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Online education, health policy and health delivery systems.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-7307"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-7307</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:AndyHyer@boisestate.edu"
# 			>
# 			<span class="c-btn__text">AndyHyer@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/ahyer/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio Andy Hyer</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Online education, health policy and health delivery systems.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Jen Intelicato headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2021/08/Intelicato-Jen_profile-pic.jpeg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Jennifer Intelicato

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Biomedical Science, infectious disease, proteomics, online learning and instruction and online course development</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5065"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5065</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:jenniferintelicato@boisestate.edu"
# 			>
# 			<span class="c-btn__text">jenniferintelicato@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/jennifer-intelicato-ms/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Jennifer Intelicato</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Biomedical Science, infectious disease, proteomics, online learning and instruction and online course development</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Kirk Ketelsen headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Kirk-Ketelsen-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Kirk Ketelsen, PhD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Associate Professor, Health Data Analytics Program Director, DASH Lab Director

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Statistics, data science education, storytelling with data and data visualization, using data to drive evidence-based practice and decision-making.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 104

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2333"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2333</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:KirkKetelsen@boisestate.edu"
# 			>
# 			<span class="c-btn__text">KirkKetelsen@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/kirk-ketelsen-ph-d/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Kirk Ketelsen</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Statistics, data science education, storytelling with data and data visualization, using data to drive evidence-based practice and decision-making.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Nichole Lasich headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Nichole-Lasich-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Nichole Lasich, BSN, MPH

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Associate Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Assist students to be their most authentic selves and reach their professional goals, incorporate intersectionality into the biomedical paradigm and promote public health.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 114

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3912"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3912</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:nicholelasich@boisestate.edu"
# 			>
# 			<span class="c-btn__text">nicholelasich@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/nlasich/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Nichole Lasich</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Assist students to be their most authentic selves and reach their professional goals, incorporate intersectionality into the biomedical paradigm and promote public health.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Joanna McCormack headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Joanna-McCormack-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Joanna McCormack, MHS, MS, CCA

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Epidemiology, maternal and infant health, data analytics and visualization, application of state and federal healthcare policy, health information management, online instruction and online course design</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2189"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2189</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:joannamccormack@boisestate.edu"
# 			>
# 			<span class="c-btn__text">joannamccormack@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/joanna-mccormack-mhs-ms-cca/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Joanna McCormack</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Epidemiology, maternal and infant health, data analytics and visualization, application of state and federal healthcare policy, health information management, online instruction and online course design</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Douglas J. Myers headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Luke-Montrose-Headshot-3.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Douglas J. Myers, ScD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Professor, PhD Program Director

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Occupational epidemiology, workplace injury, workplace safety, healthcare workers and social determinants of health.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 111

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-4289"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-4289</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:douglasmyers@boisestate.edu"
# 			>
# 			<span class="c-btn__text">douglasmyers@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/douglas-myers/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Douglas J. Myers</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Occupational epidemiology, workplace injury, workplace safety, healthcare workers and social determinants of health.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Taylor Neher headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2022/09/Headshot.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Taylor Neher, DrPH, MPH

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Community evaluations and building community leadership; Youth, Young Adults, and Carceral Populations and their Mental Health; and historically Underserved populations.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 115

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5067"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5067</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:taylorneher@boisestate.edu"
# 			>
# 			<span class="c-btn__text">taylorneher@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href=" https://www.boisestate.edu/spph/taylor-neher-drph-mph/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Taylor Neher</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Community evaluations and building community leadership; Youth, Young Adults, and Carceral Populations and their Mental Health; and historically Underserved populations.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Kimberley Rauscher headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Kimberley-Rauscher-Headshot.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Kimberly Rauscher, ScD, MA

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: HIV prevention and control; emerging infectious diseases; post-disaster health outcomes; global health diplomacy; the dynamic relationships between infectious agents, their hosts, and the environment in which these interactions occur; the international dialogue on disease prevention (including international binding and non-binding instruments and their negotiation and application) and highlighting how the interconnectedness of today&#8217;s world reveals the global nature of public health issues.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 122A

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2335"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2335</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:kimberlyrauscher@boisestate.edu"
# 			>
# 			<span class="c-btn__text">kimberlyrauscher@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/kimberly-rauscher/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Kimberly Rauscher</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: HIV prevention and control; emerging infectious diseases; post-disaster health outcomes; global health diplomacy; the dynamic relationships between infectious agents, their hosts, and the environment in which these interactions occur; the international dialogue on disease prevention (including international binding and non-binding instruments and their negotiation and application) and highlighting how the interconnectedness of today&#8217;s world reveals the global nature of public health issues.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Uwe Reischl headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Uwe-Reischl-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Uwe Reischl, PhD, MD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Occupational health, ergonomics, human factors and telemedicine.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 105

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2445"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2445</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:ureischl@boisestate.edu"
# 			>
# 			<span class="c-btn__text">ureischl@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/ureischl/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Uwe Reischl</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Occupational health, ergonomics, human factors and telemedicine.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Ellen Schafer headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Ellen-Schafer-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Ellen Schafer, PhD, MPH, MCHES

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Associate Professor, MPH Program Director

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Influence of social context, social networks and social support on behaviors related to maternal child health and caregiving</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 107

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5288"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5288</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:ellenschafer@boisestate.edu"
# 			>
# 			<span class="c-btn__text">ellenschafer@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/ellen-schafer/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Ellen Schafer</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Influence of social context, social networks and social support on behaviors related to maternal child health and caregiving</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Megan Smith headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Megan-Smith-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Megan L. Smith, PhD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Associate Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Education, human development, and public health science to study the contextual factors that promote or thwart health outcomes (particularly substance use, mental health, and sexual risk behavior) for young people.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 108

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3335"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3335</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:mlsmith@boisestate.edu"
# 			>
# 			<span class="c-btn__text">mlsmith@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/megan-smith-phd/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Megan L. Smith</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Education, human development, and public health science to study the contextual factors that promote or thwart health outcomes (particularly substance use, mental health, and sexual risk behavior) for young people.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Tom Turco headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Tom-Turco-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Tom Turco, MS, REHS, ASP

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Clinical Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Environmental health, public health emergency response, integration of online educational resources in lieu of textbooks and development of Pressbook textbooks for classes.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Hybrid

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3908"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3908</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:ThomasTurco@boisestate.edu"
# 			>
# 			<span class="c-btn__text">ThomasTurco@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/tturco/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Tom Turco</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Environmental health, public health emergency response, integration of online educational resources in lieu of textbooks and development of Pressbook textbooks for classes.</p>

# </div>

# 						</li>
					
# 				</ul>
# 			</div>

		
				
# 		</div>
# </div>

# 			</div>
	




# 			<div class="panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding"
# 				 data-index=""
# 				 data-js="panel"
# 				 data-type="people-list"
			     
# 				 data-modular-content>
	
# 	<div class="site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding">
# 	<div class="l-content--inner">
		
	
# 				<div class="oneUp">
# 				<header class="s-header t-content">
					
# <h2
# 		class="site-panel__title s-title h2"
# 		>

# 	Research Faculty

# </h2>
					
# 				</header>
# 			</div>
# 			<div class="s-content">
# 				<ul class="panel-people__listing oneUp">

# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2025/01/Kelley_George-1152x1440.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	George Kelley, FACSM

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Research Professor 

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of Interest: Systematic reviews, meta-analysis, exercise, physical activity, health related disease</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5066"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5066</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:georgekelley@boisestate.edu"
# 			>
# 			<span class="c-btn__text">georgekelley@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/george-a-kelley-facsm/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for George Kelley</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of Interest: Systematic reviews, meta-analysis, exercise, physical activity, health related disease</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2025/01/Kelley_Kristi-1152x1440.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Kristi Kelley, M.Ed.

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Research Assistant Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:kristikelley@boisestate.edu"
# 			>
# 			<span class="c-btn__text">kristikelley@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/kristi-kelley-m-ed/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Kristi Kelley</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease</p>

# </div>

# 						</li>
					
# 				</ul>
# 			</div>

		
				
# 		</div>
# </div>

# 			</div>
	




# 			<div class="panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding"
# 				 data-index=""
# 				 data-js="panel"
# 				 data-type="people-list"
			     
# 				 data-modular-content>
	
# 	<div class="site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding">
# 	<div class="l-content--inner">
		
	
# 				<div class="one_up">
# 				<header class="s-header t-content">
					
# <h2
# 		class="site-panel__title s-title h2"
# 		>

# 	Faculty Emeriti

# </h2>
					
# 				</header>
# 			</div>
# 			<div class="s-content">
# 				<ul class="panel-people__listing one_up">

# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Sarah Toevs headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Sarah-Toevs-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Sarah Toevs, PhD

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Emeritus Professor, School of Public and Population Health

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Program evaluation and assessment and generating real-time evidence for use in community-based planning and decision making.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		>

	
# <a class=""
# 			href="mailto:stoevs@boisestate.edu"
# 			>
# 			<span class="c-btn__text">stoevs@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://docs.google.com/document/d/1UAdyRExs8TUunlcwXyhT8dzussmiVtJN-16ra5s5o5g/edit"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Curriculum Vitae</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Program evaluation and assessment and generating real-time evidence for use in community-based planning and decision making.</p>

# </div>

# 						</li>
					
# 				</ul>
# 			</div>

		
				
# 		</div>
# </div>

# 			</div>
	




# 			<div class="panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding"
# 				 data-index=""
# 				 data-js="panel"
# 				 data-type="people-list"
			     
# 				 data-modular-content>
	
# 	<div class="site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding">
# 	<div class="l-content--inner">
		
	
# 				<div class="oneUp">
# 				<header class="s-header t-content">
					
# <h2
# 		class="site-panel__title s-title h2"
# 		>

# 	Affiliate Faculty

# </h2>
					
# 				</header>
# 			</div>
# 			<div class="s-content">
# 				<ul class="panel-people__listing oneUp">

# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Traci Berreth" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/11/T.Berreth_2023-1152x926.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Traci Berreth

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Affiliate Faculty &amp; Deputy Division Administrator at ID Department of Health and Welfare

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Public Health Policy, Strategy and Systems Thinking, Effective Communication and Relationship Building, and Leadership.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:TraciBerreth@boisestate.edu"
# 			>
# 			<span class="c-btn__text">TraciBerreth@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/traci-berreth-phd-mph-spph-affiliate-faculty/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Traci Berreth</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Public Health Policy, Strategy and Systems Thinking, Effective Communication and Relationship Building, and Leadership.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Matt Isbell" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/10/matt-1152x1620.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Matt Isbell

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Affiliate Faculty &amp; Department of Communication Professor

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Collaboration, nonprofit organizations and program implementation/change</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	COMB 220

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 960-0204"
# 			>
# 			<span class="c-btn__text">Call: (208) 960-0204</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:matthewisbell@boisestate.edu"
# 			>
# 			<span class="c-btn__text">matthewisbell@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/dept-communication/department-faculty-and-staff/dr-matt-isbell-2/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Matt Isbell</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Collaboration, nonprofit organizations and program implementation/change</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Bozena Morawski" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/10/Morawski_Headshot.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Bozena Morawski

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Affiliate Faculty &amp; Epidemiologist

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:bozenamorawski@boisestate.edu"
# 			>
# 			<span class="c-btn__text">bozenamorawski@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/bozena-m-morawski-mph-phd/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Bozena Morawski</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Ingrid Rabe, SPPH Affiliate Faculty" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2024/07/I-Rabe_ii-1152x1376.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Ingrid Rabe

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Affiliate Faculty &amp; Medical Epidemiologist, Arboviruses

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Applied epidemiology, vector-borne diseases, tropical medicine, outbreak response, disease surveillance evaluation and technical guidance development.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:ingridrabe@boisestate.edu"
# 			>
# 			<span class="c-btn__text">ingridrabe@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/ingrid-rabe-mbchb-mmed-spph-affiliate-faculty/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Ingrid Rabe</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Applied epidemiology, vector-borne diseases, tropical medicine, outbreak response, disease surveillance evaluation and technical guidance development.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Vinita Sharma headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/01/Sharma_Vinita.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Vinita Sharma

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Affiliate Faculty 

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: <span style="font-weight: 400">Intersection between substance use, HIV and mental health, reproductive health, adolescent and youth health, infectious diseases, post-disaster health outcomes and global health</span></p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:vinitasharma@boisestate.edu"
# 			>
# 			<span class="c-btn__text">vinitasharma@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="https://www.boisestate.edu/spph/vinita-sharma-phd-mph-cph-ches/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Vinita Sharma</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: <span style="font-weight: 400">Intersection between substance use, HIV and mental health, reproductive health, adolescent and youth health, infectious diseases, post-disaster health outcomes and global health</span></p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Elke Shaw-Tulloch Headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/12/Elke-Shaw-Tulloch-Headshot-color.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Elke Shaw-Tulloch

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Affiliate Faculty &amp; State Health Official

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Public health, public health policy, social determinants of health, environmental health, public health emergency response, strategy and systems thinking, communication and relationship building.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Remote

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto: elkeshawtulloch@boisestate.edu"
# 			>
# 			<span class="c-btn__text"> elkeshawtulloch@boisestate.edu</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href=" https://www.boisestate.edu/spph/elke-shaw-tulloch-mhs/"
# 			target="_blank"
# 		rel='noopener'>
# 			<span class="c-btn__text">Full Bio for Elke Shaw-Tulloch</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Public health, public health policy, social determinants of health, environmental health, public health emergency response, strategy and systems thinking, communication and relationship building.</p>

# </div>

# 						</li>
					
# 				</ul>
# 			</div>

		
				
# 		</div>
# </div>

# 			</div>
	




# 			<div class="panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding"
# 				 data-index=""
# 				 data-js="panel"
# 				 data-type="people-list"
			     
# 				 data-modular-content>
	
# 	<div class="site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding">
# 	<div class="l-content--inner">
		
	
# 				<div class="oneUp">
# 				<header class="s-header t-content">
					
# <h2
# 		class="site-panel__title s-title h2"
# 		>

# 	Staff

# </h2>
					
# 				</header>
# 			</div>
# 			<div class="s-content">
# 				<ul class="panel-people__listing oneUp">

# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2025/02/Deependra-Dehariya_Boise-1152x1731.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Deependra Dehariya

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Special Project Coordinator for Data-Driven, Community-Engaged, Global Partnerships

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Supporting initiatives that enhance public and population health. Experience in project management, data analysis, digital marketing, process optimization and stakeholder engagement. Supporting data-driven, community-engaged projects to drive meaningful impact, implementing evidence-based strategies like the Icelandic Prevention Model to improve youth well-being as part of initiatives like Communities for Youth (C4Y).</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:deependradehariya@boisestate.edu"
# 			>
# 			<span class="c-btn__text">deependradehariya@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Supporting initiatives that enhance public and population health. Experience in project management, data analysis, digital marketing, process optimization and stakeholder engagement. Supporting data-driven, community-engaged projects to drive meaningful impact, implementing evidence-based strategies like the Icelandic Prevention Model to improve youth well-being as part of initiatives like Communities for Youth (C4Y).</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Brendy McConnaughey" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2024/03/McConnaughey_Brendy-1152x1440.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Brendy McConnaughey

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Management Assistant

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Providing exceptional administrative support to SPPH staff, faculty and students while becoming a reliable resource to our community partners. Collaborating with team members to support the school&#8217;s events and projects.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 122

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:208-426-3929"
# 			>
# 			<span class="c-btn__text">Call: 208-426-3929</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:brendymcconnaughey@boisestate.edu"
# 			>
# 			<span class="c-btn__text">brendymcconnaughey@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Providing exceptional administrative support to SPPH staff, faculty and students while becoming a reliable resource to our community partners. Collaborating with team members to support the school&#8217;s events and projects.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Kelsey Nelson headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Kelsey-Nelson-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Kelsey Nelson

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Internship Coordinator

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Career development, job and internship application and search, interviewing, resume, cover letter and ePortfolio Development</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Boulder Hall

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-5414"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-5414</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:kelseynelson1@boisestate.edu"
# 			>
# 			<span class="c-btn__text">kelseynelson1@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Career development, job and internship application and search, interviewing, resume, cover letter and ePortfolio Development</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Hailey Stewart headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2021/12/0.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Hailey Stewart

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Senior Communications Specialist

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Supporting SPPH communications and marketing needs. Sharing student and faculty stories. Developing community building experiences and opportunities for students and the university community.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 125

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2187"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2187</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:haileystewart966@boisestate.edu"
# 			>
# 			<span class="c-btn__text">haileystewart966@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Supporting SPPH communications and marketing needs. Sharing student and faculty stories. Developing community building experiences and opportunities for students and the university community.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Maria Tellez headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Maria-Tellez-Headshots-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Maria Tellez, MHS

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Business Operations Manager

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Bridge building across various campus administrative areas, fiscal leadership, guidance and support for school strategic initiatives, community building, process improvement and how to best collaborate to support partners, those who work with us and students.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	HSRV 123

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-3922"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-3922</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:mariatellez@boisestate.edu"
# 			>
# 			<span class="c-btn__text">mariatellez@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Bridge building across various campus administrative areas, fiscal leadership, guidance and support for school strategic initiatives, community building, process improvement and how to best collaborate to support partners, those who work with us and students.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Adam Wagner headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2023/02/Wagner_Adam1.jpg" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Adam Wagner

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Student Communications Assistant

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Supporting the department’s communication needs by corresponding with students and faculty, attending and helping to facilitate events and addressing project-based tasks.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Hybrid

# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:adamwagner116@boisestate.edu"
# 			>
# 			<span class="c-btn__text">adamwagner116@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Supporting the department’s communication needs by corresponding with students and faculty, attending and helping to facilitate events and addressing project-based tasks.</p>

# </div>

# 						</li>
# 											<li class="panel-people__item">
							
# <div class="panel-people__media">
# 		<figure   class="tribe-image">
	
		
# 				<img decoding="async" class=""  alt="Brian Young headshot" role="img" src="https://www.boisestate.edu/spph/wp-content/uploads/sites/99/2020/10/Brian-Young-Headshot-1.png" />
		
		
		

# 		</figure>
# 	</div>

# <div class="panel-people__info" >
	
# <div class="panel-people__info__hd" >
	
# <h3
# 		class="panel-people__name"
# 		>

# 	Brian Young

# </h3>
# <h4
# 		class="panel-people__title"
# 		>

# 	Director of Academic Operations

# </h4>
# </div>

# <div class="panel-people__description t-content panel-people__description--mobile" >
# 	<p>Areas of interest: Online learning, learning management systems and instructional design.</p>

# </div>

# <div class="panel-people__info__ft" >
	
# <div
# 		class="panel-people__dept-location"
# 		>

# 	Hybrid

# </div>
# <div
# 		>

	
# <a class=""
# 			href="tel:(208) 426-2140"
# 			>
# 			<span class="c-btn__text">Call: (208) 426-2140</span>
# 	</a>


# </div>
# <div
# 		>

	
# <a class=""
# 			href="mailto:brianyoung651@boisestate.edu"
# 			>
# 			<span class="c-btn__text">brianyoung651@boisestate.edu</span>
# 	</a>


# </div>
# </div>

# </div>

# <div class="panel-people__description t-content panel-people__description--desktop" >
# 	<p>Areas of interest: Online learning, learning management systems and instructional design.</p>

# </div>

# 						</li>
					
# 				</ul>
# 			</div>

		
				
# 		</div>
# </div>

# 			</div>
	

# </div>

					
# 	</div>
	

# </main>


	
# 						<section class="footer-contact" role="complementary" aria-label="Contact Information">
# 					<div class="footer-contact__contain">
# 									<div class="footer-contact__name">
# 						<h2>School of Public and Population Health</h2>
# 					</div>
# 													<div class="footer-contact__email">
# 						<a href="mailto:spph@boisestate.edu">spph@boisestate.edu</a>
# 					</div>
# 													<div class="footer-contact__phone">
# 						<a href="tel:208-426-3929">208-426-3929</a>
# 					</div>
# 													<div class="footer-contact__address">
# 													Health Sciences Riverside, Room 122
# 											</div>
# 							</div>
# 							<div class="footer-contact__contain footer-contact__social">
# 				<div class="footer-contact__name footer-contact__social-name">
# 					Follow Us
# 				</div>
# 				<ul class="footer-contact__social-list">
# 											<li class="footer-contact__social-item">
# 							<a href="https://twitter.com/BoiseStateSPPH" target="_blank" rel="noopener">
# 								<i class="icon icon-x" role="img"></i>
# 								<span class="u-screen-reader-text">Follow us on X</span>
# 							</a>
# 						</li>
# 																<li class="footer-contact__social-item">
# 							<a href="https://www.facebook.com/BoiseStateUniversitySPPH" target="_blank" rel="noopener">
# 								<i class="icon icon-facebook" role="img"></i>
# 								<span class="u-screen-reader-text">Follow us on Facebook</span>
# 							</a>
# 						</li>
# 																<li class="footer-contact__social-item">
# 							<a href="https://www.instagram.com/boisestatespph/" target="_blank" rel="noopener">
# 								<i class="icon icon-instagram2" role="img"></i>
# 								<span class="u-screen-reader-text">Follow us on Instagram</span>
# 							</a>
# 						</li>
# 																					<li class="footer-contact__social-item">
# 							<a href="https://www.linkedin.com/showcase/college-of-health-sciences/" target="_blank" rel="noopener">
# 								<i class="icon icon-linkedin" role="img"></i>
# 								<span class="u-screen-reader-text">Follow us on Linkedin</span>
# 							</a>
# 						</li>
# 									</ul>
# 			</div>
# 					</section>

# <footer class="site-footer">

# 	<div class="l-container l-container--inner">

		
# 	<nav class="site-footer__nav" aria-labelledby="site-footer__nav-label">

# 		<h2 id="site-footer__nav-label" class="u-visual-hide">Secondary Navigation</h2>

# 		<ul class="site-footer__nav-list">
# 			<li class="secondary__list-item secondary__list-item--depth-0"><a href="https://my.boisestate.edu/" class="site-nav__action secondary__action secondary__action--depth-0">myBoiseState</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/safety/" class="site-nav__action secondary__action secondary__action--depth-0">Safety, Security and Support</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/jobs/" class="site-nav__action secondary__action secondary__action--depth-0">Career Opportunities</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestatepublicradio.org/" class="site-nav__action secondary__action secondary__action--depth-0">Boise State Public Radio</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/library/" class="site-nav__action secondary__action secondary__action--depth-0">Albertsons Library</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/publicsafety-transportation/" class="site-nav__action secondary__action secondary__action--depth-0">Transportation and Parking</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/partnerships/" class="site-nav__action secondary__action secondary__action--depth-0">Partner with Us</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.morrisoncenter.com/" class="site-nav__action secondary__action secondary__action--depth-0">Morrison Center</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/alumni" class="site-nav__action secondary__action secondary__action--depth-0">Alumni</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.broncoshop.com/" class="site-nav__action secondary__action secondary__action--depth-0">Bronco Shop and Bookstore</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.boisestate.edu/president/about/university-leadership/" class="site-nav__action secondary__action secondary__action--depth-0">University Administration</a></li><li class="secondary__list-item secondary__list-item--depth-0"><a href="https://www.extramilearena.com/" class="site-nav__action secondary__action secondary__action--depth-0">ExtraMile Arena</a></li>
# 		</ul>

# 		<a href="https://www.broncosports.com/" target="_blank" class="site-footer__nav-logo">
# 			<span class="icon">
# 				<span class="u-visual-hide">Broncos Logo</span>
# 			</span>
# 			<span class="site-footer__nav-logo__heading">
# 				<span>Athletics<span>
# 			</span>
# 		</a>
# 	</nav>



# 		<div class="site-footer__under">

# 			<div class="social-follow">

# 	<ul class="social-follow__list">

# 				<li class="social-follow__item">
# 			<a href="https://www.facebook.com/BoiseStateUniversity" class="social-follow__anchor" rel="me noopener" title="Follow us on Facebook" target="_blank">
# 				<i class="icon icon-facebook"></i>
# 				<span class="u-visual-hide">Follow us on Facebook</span>
# 			</a>
# 		</li>
		
# 				<li class="social-follow__item">
# 			<a href="https://www.instagram.com/boisestateuniversity/" class="social-follow__anchor" rel="me noopener" title="Follow us on Instagram" target="_blank">
# 				<i class="icon icon-instagram"></i>
# 				<span class="u-visual-hide">Follow us on Instagram</span>
# 			</a>
# 		</li>
		
# 				<li class="social-follow__item">
# 			<a href="https://twitter.com/BoiseState" class="social-follow__anchor" rel="me noopener" title="Follow us on X" target="_blank">
# 				<i class="icon icon-x"></i>
# 				<span class="u-visual-hide">Follow us on X</span>
# 			</a>
# 		</li>
		
# 				<li class="social-follow__item">
# 			<a href="https://www.youtube.com/user/BoiseStateUniversity" class="social-follow__anchor" rel="me noopener" title="Follow us on Youtube" target="_blank">
# 				<i class="icon icon-youtube"></i>
# 				<span class="u-visual-hide">Follow us on Youtube</span>
# 			</a>
# 		</li>
		
# 				<li class="social-follow__item">
# 			<a href="https://www.linkedin.com/school/boisestate/" class="social-follow__anchor" rel="me noopener" title="Follow us on LinkedIn" target="_blank">
# 				<i class="icon icon-linkedin"></i>
# 				<span class="u-visual-hide">Follow us on LinkedIn</span>
# 			</a>
# 		</li>
# 			</ul>

# </div>


# 			<div class="site-footer__utility">
# 				<ul class="site-footer__utility__nav">
# 					<li class="footer_util__list-item footer_util__list-item--depth-0"><a href="https://www.boisestate.edu/terms-of-use/" class="site-nav__action footer_util__action footer_util__action--depth-0">Terms of Use</a></li><li class="footer_util__list-item footer_util__list-item--depth-0"><a href="https://www.boisestate.edu/accessibility/" class="site-nav__action footer_util__action footer_util__action--depth-0">Accessibility</a></li><li class="footer_util__list-item footer_util__list-item--depth-0"><a href="https://www.boisestate.edu/privacy" class="site-nav__action footer_util__action footer_util__action--depth-0">Privacy</a></li><li class="footer_util__list-item footer_util__list-item--depth-0"><a href="https://www.boisestate.edu/classroomconcerns/" class="site-nav__action footer_util__action footer_util__action--depth-0">Classroom Concerns</a></li><li class="footer_util__list-item footer_util__list-item--depth-0"><a href="https://www.boisestate.edu/policy/" class="site-nav__action footer_util__action footer_util__action--depth-0">Policies</a></li><li class="footer_util__list-item footer_util__list-item--depth-0"><a href="https://www.boisestate.edu/contact/" class="site-nav__action footer_util__action footer_util__action--depth-0">Contact Boise State</a></li>
# 				</ul>

# 				<p class="site-footer__copyright">
# 					<a href="https://www.boisestate.edu/" rel="external">
# 					    &copy; 2025 All Rights Reserved
# 						 Boise State University.
# 					</a>
# 				</p>
# 			</div>
# 		</div>

# 	</div>

# </footer>

		
	
	
	

	

# 	<script type="application/ld+json">{
#     "@context": "https:\/\/schema.org",
#     "@type": "Organization",
#     "name": "",
#     "logo": [],
#     "url": "https:\/\/www.boisestate.edu\/spph",
#     "sameAs": [
#         "https:\/\/plus.google.com\/u\/0\/115379189893046057301",
#         "https:\/\/www.linkedin.com\/company\/modern-tribe-inc-",
#         "https:\/\/www.facebook.com\/ModernTribeInc\/"
#     ]
# }</script><script type="application/ld+json">{
#     "@context": "https:\/\/schema.org",
#     "@type": "WebPage",
#     "mainEntityOfPage": {
#         "@type": "WebPage",
#         "@id": "https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/"
#     },
#     "datePublished": "2019-12-18 13:54:21",
#     "dateModified": "2025-02-19 10:20:29",
#     "description": "",
#     "name": "Faculty and Staff Directory",
#     "headline": "Faculty and Staff Directory",
#     "copyrightHolder": "",
#     "creator": "",
#     "image": [],
#     "thumbnailUrl": "",
#     "url": "https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/",
#     "text": "\n<p><a class=\"c-btn\" href=\"https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-online-request-forms\/\">Faculty &amp; Staff Online Forms<\/a><\/p>\n\n\n\n\n\t\t\t<div class=\"panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding\"\n\t\t\t\t data-index=\"\"\n\t\t\t\t data-js=\"panel\"\n\t\t\t\t data-type=\"people-list\"\n\t\t\t     \n\t\t\t\t data-modular-content>\n\t\n\t<div class=\"site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding\">\n\t<div class=\"l-content--inner\">\n\t\t\n\t\n\t\t\t\t<div class=\"oneUp\">\n\t\t\t\t<header class=\"s-header t-content\">\n\t\t\t\t\t\n<h2\n\t\tclass=\"site-panel__title s-title h2\"\n\t\t>\n\n\tFaculty\n\n<\/h2>\n\t\t\t\t\t\n\t\t\t\t<\/header>\n\t\t\t<\/div>\n\t\t\t<div class=\"s-content\">\n\t\t\t\t<ul class=\"panel-people__listing oneUp\">\n\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Mike Mann headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Mike-Mann-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tMike Mann, PhD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tSPPH Director and Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: The intersection between public health and public schooling, academic achievement as a social determinant of health, student mental health promotion and school\/community substance abuse prevention partnerships.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 112\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3334\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3334<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:mikemann@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">mikemann@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/mikemann\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Mike Mann<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: The intersection between public health and public schooling, academic achievement as a social determinant of health, student mental health promotion and school\/community substance abuse prevention partnerships.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Mac McCullough headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2022\/10\/McCullough_Mac.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tMac McCullough, PhD, MPH\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tProfessor and Associate Director for Community Engagement and Impact\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p><span style=\"font-weight: 400\">Areas of interest: Health finance, health policy including value-based care, public health economics, social determinants of health, health management, academic health departments, healthcare analytics and health IT.<\/span><\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 106\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3923\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3923<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:macmccullough@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">macmccullough@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/mac-mccullough-phd-mph\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Mac McCullough<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p><span style=\"font-weight: 400\">Areas of interest: Health finance, health policy including value-based care, public health economics, social determinants of health, health management, academic health departments, healthcare analytics and health IT.<\/span><\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Jaime Sand headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Jaime-Sand-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tJaime Sand, EdD, RHIA, CCS, CAHIMS\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tProfessor and Associate Director for Student Engagement and Impact\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Online and undergraduate curriculum and instruction, health information education, interprofessional education, medical coding training and nontraditional student engagement<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 109\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5392\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5392<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:jaimesand@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">jaimesand@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/jsand\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Jaime Sand<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Online and undergraduate curriculum and instruction, health information education, interprofessional education, medical coding training and nontraditional student engagement<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Anne Abbott\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/08\/IMG_7453-1-1152x1252.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tAnne Abbott, PhD, MPP\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Health Communication, Public Health Policy, Program Planning and Evaluation, Violence Prevention, and Adolescent and Young Adult Health.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 113\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5061\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5061<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:anneabbott@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">anneabbott@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/anne-abbot-phd-mpp\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Anne Abbott<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Health Communication, Public Health Policy, Program Planning and Evaluation, Violence Prevention, and Adolescent and Young Adult Health.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Travis Armstrong\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2024\/07\/Armstrong_Travis-1152x1440.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tTravis Armstrong, MPA, RT (R)\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Associate Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p><span style=\"font-weight: 400\">Areas of Interest: Connecting students to programs and resources that support their academic and professional journeys, eight dimensions of wellness, allied health professions, healthcare delivery in rural and underserved areas, impact of public lands and outdoor recreation on public health and wellness.<\/span><\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 102\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5062\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5062<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:travisarmstrong@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">travisarmstrong@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/travis-armstrong-rtr\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Travis Armstrong<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p><span style=\"font-weight: 400\">Areas of Interest: Connecting students to programs and resources that support their academic and professional journeys, eight dimensions of wellness, allied health professions, healthcare delivery in rural and underserved areas, impact of public lands and outdoor recreation on public health and wellness.<\/span><\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Ed Baker headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Ed-Baker-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tEd Baker, PhD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tProfessor \n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Healthcare policy, rural workforce planning, healthcare financing and performance improvement.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tYanke Family Research Park 903\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3118\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3118<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:ebaker@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">ebaker@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/e-baker\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Ed Baker<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Healthcare policy, rural workforce planning, healthcare financing and performance improvement.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Desmond Banks headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Desmond-Banks-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tDesmond Banks, PhD, MPH\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Assistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Social determinants of health, health disparities, health equity, chronic disease and program evaluation.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5063\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5063<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:desmondbanks@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">desmondbanks@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/desmond-banks-phd-mph\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio For Desmond Banks<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Social determinants of health, health disparities, health equity, chronic disease and program evaluation.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Kruti Chaliawala\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2024\/08\/Headshot_3-1152x1728.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tKruti Chaliawala, PhD, MS, MA, CHES\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of Interest: Psychosocial determinants of health behaviors among adolescents and young adults, sexual health, mental health, international student health disparities and minority health.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 103\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3921\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3921<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:krutichaliawala@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">krutichaliawala@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/kruti-chaliawala-phd-ms-ma-ches\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Kruti Chaliawala<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of Interest: Psychosocial determinants of health behaviors among adolescents and young adults, sexual health, mental health, international student health disparities and minority health.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Cynthia Curl headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Cynthia-Curl-Headshot-2.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tCynthia Curl, PhD, MS\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssociate Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Measuring human exposures to agricultural chemicals and improving health and safety in agricultural workplaces and agricultural communities. Student intern and volunteer positions are available in the Curl Agricultural Health lab.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3924\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3924<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:cynthiacurl@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">cynthiacurl@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/ccurl\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Cynthia Curl<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Measuring human exposures to agricultural chemicals and improving health and safety in agricultural workplaces and agricultural communities. Student intern and volunteer positions are available in the Curl Agricultural Health lab.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2025\/02\/Priyanka-Dubey-1152x1440.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\t Priyanka Dubey, PhD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Sexual and reproductive health and menstrual health of gender diverse communities, maternal and child health, global health<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 121\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5064\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5064<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:priyankadubey@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">priyankadubey@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/priyanka-dubey-phd\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for  Priyanka Dubey<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Sexual and reproductive health and menstrual health of gender diverse communities, maternal and child health, global health<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Ashley Havlicak\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2024\/01\/0-e1715637604494.webp\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tAshley Havlicak, MPH\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Assistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Policy, environment and systems change, school and adolescent health, mental health, health equity, social influencers of health, project management, collective impact and collaboration.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 124\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2188\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2188<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:ashleyhavlicak@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">ashleyhavlicak@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/ashley-havlicak-mph\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Ashley Havlicak<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Policy, environment and systems change, school and adolescent health, mental health, health equity, social influencers of health, project management, collective impact and collaboration.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2025\/02\/unnamed.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tAndrea Hill, MPH, RD, LD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssistant Teaching Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Community engagement strategies, youth mental health and well-being, public health nutrition issues, and the social determinants of health.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 124\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:andreahill565@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">andreahill565@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/andrea-hill-mph-rd-ld\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Andrea Hill<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Community engagement strategies, youth mental health and well-being, public health nutrition issues, and the social determinants of health.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Andy Hyer\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Andy-Hyer-Headshot-2.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tAndy Hyer, JD, MHS\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Associate Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Online education, health policy and health delivery systems.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-7307\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-7307<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:AndyHyer@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">AndyHyer@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/ahyer\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio Andy Hyer<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Online education, health policy and health delivery systems.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Jen Intelicato headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2021\/08\/Intelicato-Jen_profile-pic.jpeg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tJennifer Intelicato\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Assistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Biomedical Science, infectious disease, proteomics, online learning and instruction and online course development<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5065\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5065<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:jenniferintelicato@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">jenniferintelicato@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/jennifer-intelicato-ms\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Jennifer Intelicato<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Biomedical Science, infectious disease, proteomics, online learning and instruction and online course development<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Kirk Ketelsen headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Kirk-Ketelsen-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tKirk Ketelsen, PhD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Associate Professor, Health Data Analytics Program Director, DASH Lab Director\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Statistics, data science education, storytelling with data and data visualization, using data to drive evidence-based practice and decision-making.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 104\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2333\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2333<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:KirkKetelsen@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">KirkKetelsen@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/kirk-ketelsen-ph-d\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Kirk Ketelsen<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Statistics, data science education, storytelling with data and data visualization, using data to drive evidence-based practice and decision-making.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Nichole Lasich headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Nichole-Lasich-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tNichole Lasich, BSN, MPH\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Associate Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Assist students to be their most authentic selves and reach their professional goals, incorporate intersectionality into the biomedical paradigm and promote public health.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 114\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3912\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3912<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:nicholelasich@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">nicholelasich@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/nlasich\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Nichole Lasich<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Assist students to be their most authentic selves and reach their professional goals, incorporate intersectionality into the biomedical paradigm and promote public health.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Joanna McCormack headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Joanna-McCormack-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tJoanna McCormack, MHS, MS, CCA\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Assistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Epidemiology, maternal and infant health, data analytics and visualization, application of state and federal healthcare policy, health information management, online instruction and online course design<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2189\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2189<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:joannamccormack@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">joannamccormack@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/joanna-mccormack-mhs-ms-cca\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Joanna McCormack<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Epidemiology, maternal and infant health, data analytics and visualization, application of state and federal healthcare policy, health information management, online instruction and online course design<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Douglas J. Myers headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Luke-Montrose-Headshot-3.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tDouglas J. Myers, ScD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tProfessor, PhD Program Director\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Occupational epidemiology, workplace injury, workplace safety, healthcare workers and social determinants of health.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 111\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-4289\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-4289<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:douglasmyers@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">douglasmyers@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/douglas-myers\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Douglas J. Myers<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Occupational epidemiology, workplace injury, workplace safety, healthcare workers and social determinants of health.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Taylor Neher headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2022\/09\/Headshot.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tTaylor Neher, DrPH, MPH\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Community evaluations and building community leadership; Youth, Young Adults, and Carceral Populations and their Mental Health; and historically Underserved populations.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 115\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5067\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5067<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:taylorneher@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">taylorneher@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\" https:\/\/www.boisestate.edu\/spph\/taylor-neher-drph-mph\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Taylor Neher<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Community evaluations and building community leadership; Youth, Young Adults, and Carceral Populations and their Mental Health; and historically Underserved populations.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Kimberley Rauscher headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Kimberley-Rauscher-Headshot.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tKimberly Rauscher, ScD, MA\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tProfessor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: HIV prevention and control; emerging infectious diseases; post-disaster health outcomes; global health diplomacy; the dynamic relationships between infectious agents, their hosts, and the environment in which these interactions occur; the international dialogue on disease prevention (including international binding and non-binding instruments and their negotiation and application) and highlighting how the interconnectedness of today&#8217;s world reveals the global nature of public health issues.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 122A\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2335\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2335<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:kimberlyrauscher@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">kimberlyrauscher@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/kimberly-rauscher\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Kimberly Rauscher<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: HIV prevention and control; emerging infectious diseases; post-disaster health outcomes; global health diplomacy; the dynamic relationships between infectious agents, their hosts, and the environment in which these interactions occur; the international dialogue on disease prevention (including international binding and non-binding instruments and their negotiation and application) and highlighting how the interconnectedness of today&#8217;s world reveals the global nature of public health issues.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Uwe Reischl headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Uwe-Reischl-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tUwe Reischl, PhD, MD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tProfessor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Occupational health, ergonomics, human factors and telemedicine.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 105\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2445\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2445<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:ureischl@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">ureischl@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/ureischl\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Uwe Reischl<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Occupational health, ergonomics, human factors and telemedicine.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Ellen Schafer headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Ellen-Schafer-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tEllen Schafer, PhD, MPH, MCHES\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssociate Professor, MPH Program Director\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Influence of social context, social networks and social support on behaviors related to maternal child health and caregiving<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 107\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5288\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5288<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:ellenschafer@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">ellenschafer@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/ellen-schafer\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Ellen Schafer<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Influence of social context, social networks and social support on behaviors related to maternal child health and caregiving<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Megan Smith headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Megan-Smith-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tMegan L. Smith, PhD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAssociate Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Education, human development, and public health science to study the contextual factors that promote or thwart health outcomes (particularly substance use, mental health, and sexual risk behavior) for young people.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 108\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3335\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3335<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:mlsmith@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">mlsmith@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/megan-smith-phd\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Megan L. Smith<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Education, human development, and public health science to study the contextual factors that promote or thwart health outcomes (particularly substance use, mental health, and sexual risk behavior) for young people.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Tom Turco headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Tom-Turco-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tTom Turco, MS, REHS, ASP\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tClinical Assistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Environmental health, public health emergency response, integration of online educational resources in lieu of textbooks and development of Pressbook textbooks for classes.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHybrid\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3908\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3908<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:ThomasTurco@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">ThomasTurco@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/tturco\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Tom Turco<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Environmental health, public health emergency response, integration of online educational resources in lieu of textbooks and development of Pressbook textbooks for classes.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\n\t\t\t\t<\/ul>\n\t\t\t<\/div>\n\n\t\t\n\t\t\t\t\n\t\t<\/div>\n<\/div>\n\n\t\t\t<\/div>\n\t\n\n\n\n\n\t\t\t<div class=\"panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding\"\n\t\t\t\t data-index=\"\"\n\t\t\t\t data-js=\"panel\"\n\t\t\t\t data-type=\"people-list\"\n\t\t\t     \n\t\t\t\t data-modular-content>\n\t\n\t<div class=\"site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding\">\n\t<div class=\"l-content--inner\">\n\t\t\n\t\n\t\t\t\t<div class=\"oneUp\">\n\t\t\t\t<header class=\"s-header t-content\">\n\t\t\t\t\t\n<h2\n\t\tclass=\"site-panel__title s-title h2\"\n\t\t>\n\n\tResearch Faculty\n\n<\/h2>\n\t\t\t\t\t\n\t\t\t\t<\/header>\n\t\t\t<\/div>\n\t\t\t<div class=\"s-content\">\n\t\t\t\t<ul class=\"panel-people__listing oneUp\">\n\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2025\/01\/Kelley_George-1152x1440.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tGeorge Kelley, FACSM\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tResearch Professor \n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of Interest: Systematic reviews, meta-analysis, exercise, physical activity, health related disease<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5066\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5066<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:georgekelley@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">georgekelley@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/george-a-kelley-facsm\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for George Kelley<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of Interest: Systematic reviews, meta-analysis, exercise, physical activity, health related disease<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2025\/01\/Kelley_Kristi-1152x1440.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tKristi Kelley, M.Ed.\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tResearch Assistant Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:kristikelley@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">kristikelley@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/kristi-kelley-m-ed\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Kristi Kelley<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\n\t\t\t\t<\/ul>\n\t\t\t<\/div>\n\n\t\t\n\t\t\t\t\n\t\t<\/div>\n<\/div>\n\n\t\t\t<\/div>\n\t\n\n\n\n\n\t\t\t<div class=\"panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding\"\n\t\t\t\t data-index=\"\"\n\t\t\t\t data-js=\"panel\"\n\t\t\t\t data-type=\"people-list\"\n\t\t\t     \n\t\t\t\t data-modular-content>\n\t\n\t<div class=\"site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding\">\n\t<div class=\"l-content--inner\">\n\t\t\n\t\n\t\t\t\t<div class=\"one_up\">\n\t\t\t\t<header class=\"s-header t-content\">\n\t\t\t\t\t\n<h2\n\t\tclass=\"site-panel__title s-title h2\"\n\t\t>\n\n\tFaculty Emeriti\n\n<\/h2>\n\t\t\t\t\t\n\t\t\t\t<\/header>\n\t\t\t<\/div>\n\t\t\t<div class=\"s-content\">\n\t\t\t\t<ul class=\"panel-people__listing one_up\">\n\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Sarah Toevs headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Sarah-Toevs-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tSarah Toevs, PhD\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tEmeritus Professor, School of Public and Population Health\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Program evaluation and assessment and generating real-time evidence for use in community-based planning and decision making.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:stoevs@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">stoevs@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/docs.google.com\/document\/d\/1UAdyRExs8TUunlcwXyhT8dzussmiVtJN-16ra5s5o5g\/edit\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Curriculum Vitae<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Program evaluation and assessment and generating real-time evidence for use in community-based planning and decision making.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\n\t\t\t\t<\/ul>\n\t\t\t<\/div>\n\n\t\t\n\t\t\t\t\n\t\t<\/div>\n<\/div>\n\n\t\t\t<\/div>\n\t\n\n\n\n\n\t\t\t<div class=\"panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding\"\n\t\t\t\t data-index=\"\"\n\t\t\t\t data-js=\"panel\"\n\t\t\t\t data-type=\"people-list\"\n\t\t\t     \n\t\t\t\t data-modular-content>\n\t\n\t<div class=\"site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding\">\n\t<div class=\"l-content--inner\">\n\t\t\n\t\n\t\t\t\t<div class=\"oneUp\">\n\t\t\t\t<header class=\"s-header t-content\">\n\t\t\t\t\t\n<h2\n\t\tclass=\"site-panel__title s-title h2\"\n\t\t>\n\n\tAffiliate Faculty\n\n<\/h2>\n\t\t\t\t\t\n\t\t\t\t<\/header>\n\t\t\t<\/div>\n\t\t\t<div class=\"s-content\">\n\t\t\t\t<ul class=\"panel-people__listing oneUp\">\n\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Traci Berreth\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/11\/T.Berreth_2023-1152x926.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tTraci Berreth\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAffiliate Faculty &amp; Deputy Division Administrator at ID Department of Health and Welfare\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Public Health Policy, Strategy and Systems Thinking, Effective Communication and Relationship Building, and Leadership.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:TraciBerreth@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">TraciBerreth@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/traci-berreth-phd-mph-spph-affiliate-faculty\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Traci Berreth<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Public Health Policy, Strategy and Systems Thinking, Effective Communication and Relationship Building, and Leadership.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Matt Isbell\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/10\/matt-1152x1620.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tMatt Isbell\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAffiliate Faculty &amp; Department of Communication Professor\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Collaboration, nonprofit organizations and program implementation\/change<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tCOMB 220\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 960-0204\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 960-0204<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:matthewisbell@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">matthewisbell@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/dept-communication\/department-faculty-and-staff\/dr-matt-isbell-2\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Matt Isbell<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Collaboration, nonprofit organizations and program implementation\/change<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Bozena Morawski\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/10\/Morawski_Headshot.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tBozena Morawski\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAffiliate Faculty &amp; Epidemiologist\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:bozenamorawski@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">bozenamorawski@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/bozena-m-morawski-mph-phd\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Bozena Morawski<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Meta-analysis, systematic reviews, exercise, physical activity, health-related disease<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Ingrid Rabe, SPPH Affiliate Faculty\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2024\/07\/I-Rabe_ii-1152x1376.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tIngrid Rabe\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAffiliate Faculty &amp; Medical Epidemiologist, Arboviruses\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Applied epidemiology, vector-borne diseases, tropical medicine, outbreak response, disease surveillance evaluation and technical guidance development.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:ingridrabe@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">ingridrabe@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/ingrid-rabe-mbchb-mmed-spph-affiliate-faculty\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Ingrid Rabe<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Applied epidemiology, vector-borne diseases, tropical medicine, outbreak response, disease surveillance evaluation and technical guidance development.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Vinita Sharma headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/01\/Sharma_Vinita.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tVinita Sharma\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAffiliate Faculty \n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: <span style=\"font-weight: 400\">Intersection between substance use, HIV and mental health, reproductive health, adolescent and youth health, infectious diseases, post-disaster health outcomes and global health<\/span><\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:vinitasharma@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">vinitasharma@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"https:\/\/www.boisestate.edu\/spph\/vinita-sharma-phd-mph-cph-ches\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Vinita Sharma<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: <span style=\"font-weight: 400\">Intersection between substance use, HIV and mental health, reproductive health, adolescent and youth health, infectious diseases, post-disaster health outcomes and global health<\/span><\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Elke Shaw-Tulloch Headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/12\/Elke-Shaw-Tulloch-Headshot-color.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tElke Shaw-Tulloch\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tAffiliate Faculty &amp; State Health Official\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Public health, public health policy, social determinants of health, environmental health, public health emergency response, strategy and systems thinking, communication and relationship building.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tRemote\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto: elkeshawtulloch@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\"> elkeshawtulloch@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\" https:\/\/www.boisestate.edu\/spph\/elke-shaw-tulloch-mhs\/\"\n\t\t\ttarget=\"_blank\"\n\t\trel='noopener'>\n\t\t\t<span class=\"c-btn__text\">Full Bio for Elke Shaw-Tulloch<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Public health, public health policy, social determinants of health, environmental health, public health emergency response, strategy and systems thinking, communication and relationship building.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\n\t\t\t\t<\/ul>\n\t\t\t<\/div>\n\n\t\t\n\t\t\t\t\n\t\t<\/div>\n<\/div>\n\n\t\t\t<\/div>\n\t\n\n\n\n\n\t\t\t<div class=\"panel s-wrapper site-panel site-panel--people-list top-padding--add_padding bottom-padding--add_padding\"\n\t\t\t\t data-index=\"\"\n\t\t\t\t data-js=\"panel\"\n\t\t\t\t data-type=\"people-list\"\n\t\t\t     \n\t\t\t\t data-modular-content>\n\t\n\t<div class=\"site-panel__people-list panel-people l-content--outer top-padding--add_padding bottom-padding--add_padding\">\n\t<div class=\"l-content--inner\">\n\t\t\n\t\n\t\t\t\t<div class=\"oneUp\">\n\t\t\t\t<header class=\"s-header t-content\">\n\t\t\t\t\t\n<h2\n\t\tclass=\"site-panel__title s-title h2\"\n\t\t>\n\n\tStaff\n\n<\/h2>\n\t\t\t\t\t\n\t\t\t\t<\/header>\n\t\t\t<\/div>\n\t\t\t<div class=\"s-content\">\n\t\t\t\t<ul class=\"panel-people__listing oneUp\">\n\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2025\/02\/Deependra-Dehariya_Boise-1152x1731.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tDeependra Dehariya\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tSpecial Project Coordinator for Data-Driven, Community-Engaged, Global Partnerships\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Supporting initiatives that enhance public and population health. Experience in project management, data analysis, digital marketing, process optimization and stakeholder engagement. Supporting data-driven, community-engaged projects to drive meaningful impact, implementing evidence-based strategies like the Icelandic Prevention Model to improve youth well-being as part of initiatives like Communities for Youth (C4Y).<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:deependradehariya@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">deependradehariya@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Supporting initiatives that enhance public and population health. Experience in project management, data analysis, digital marketing, process optimization and stakeholder engagement. Supporting data-driven, community-engaged projects to drive meaningful impact, implementing evidence-based strategies like the Icelandic Prevention Model to improve youth well-being as part of initiatives like Communities for Youth (C4Y).<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Brendy McConnaughey\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2024\/03\/McConnaughey_Brendy-1152x1440.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tBrendy McConnaughey\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tManagement Assistant\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Providing exceptional administrative support to SPPH staff, faculty and students while becoming a reliable resource to our community partners. Collaborating with team members to support the school&#8217;s events and projects.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 122\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:208-426-3929\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: 208-426-3929<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:brendymcconnaughey@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">brendymcconnaughey@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Providing exceptional administrative support to SPPH staff, faculty and students while becoming a reliable resource to our community partners. Collaborating with team members to support the school&#8217;s events and projects.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Kelsey Nelson headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Kelsey-Nelson-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tKelsey Nelson\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tInternship Coordinator\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Career development, job and internship application and search, interviewing, resume, cover letter and ePortfolio Development<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tBoulder Hall\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-5414\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-5414<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:kelseynelson1@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">kelseynelson1@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Career development, job and internship application and search, interviewing, resume, cover letter and ePortfolio Development<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Hailey Stewart headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2021\/12\/0.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tHailey Stewart\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tSenior Communications Specialist\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Supporting SPPH communications and marketing needs. Sharing student and faculty stories. Developing community building experiences and opportunities for students and the university community.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 125\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2187\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2187<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:haileystewart966@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">haileystewart966@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Supporting SPPH communications and marketing needs. Sharing student and faculty stories. Developing community building experiences and opportunities for students and the university community.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Maria Tellez headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Maria-Tellez-Headshots-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tMaria Tellez, MHS\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tBusiness Operations Manager\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Bridge building across various campus administrative areas, fiscal leadership, guidance and support for school strategic initiatives, community building, process improvement and how to best collaborate to support partners, those who work with us and students.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHSRV 123\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-3922\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-3922<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:mariatellez@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">mariatellez@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Bridge building across various campus administrative areas, fiscal leadership, guidance and support for school strategic initiatives, community building, process improvement and how to best collaborate to support partners, those who work with us and students.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Adam Wagner headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2023\/02\/Wagner_Adam1.jpg\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tAdam Wagner\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tStudent Communications Assistant\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Supporting the department\u2019s communication needs by corresponding with students and faculty, attending and helping to facilitate events and addressing project-based tasks.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHybrid\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:adamwagner116@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">adamwagner116@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Supporting the department\u2019s communication needs by corresponding with students and faculty, attending and helping to facilitate events and addressing project-based tasks.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\t\t\t\t\t\t<li class=\"panel-people__item\">\n\t\t\t\t\t\t\t\n<div class=\"panel-people__media\">\n\t\t<figure   class=\"tribe-image\">\n\t\n\t\t\n\t\t\t\t<img decoding=\"async\" class=\"\"  alt=\"Brian Young headshot\" role=\"img\" src=\"https:\/\/www.boisestate.edu\/spph\/wp-content\/uploads\/sites\/99\/2020\/10\/Brian-Young-Headshot-1.png\" \/>\n\t\t\n\t\t\n\t\t\n\n\t\t<\/figure>\n\t<\/div>\n\n<div class=\"panel-people__info\" >\n\t\n<div class=\"panel-people__info__hd\" >\n\t\n<h3\n\t\tclass=\"panel-people__name\"\n\t\t>\n\n\tBrian Young\n\n<\/h3>\n<h4\n\t\tclass=\"panel-people__title\"\n\t\t>\n\n\tDirector of Academic Operations\n\n<\/h4>\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--mobile\" >\n\t<p>Areas of interest: Online learning, learning management systems and instructional design.<\/p>\n\n<\/div>\n\n<div class=\"panel-people__info__ft\" >\n\t\n<div\n\t\tclass=\"panel-people__dept-location\"\n\t\t>\n\n\tHybrid\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"tel:(208) 426-2140\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">Call: (208) 426-2140<\/span>\n\t<\/a>\n\n\n<\/div>\n<div\n\t\t>\n\n\t\n<a class=\"\"\n\t\t\thref=\"mailto:brianyoung651@boisestate.edu\"\n\t\t\t>\n\t\t\t<span class=\"c-btn__text\">brianyoung651@boisestate.edu<\/span>\n\t<\/a>\n\n\n<\/div>\n<\/div>\n\n<\/div>\n\n<div class=\"panel-people__description t-content panel-people__description--desktop\" >\n\t<p>Areas of interest: Online learning, learning management systems and instructional design.<\/p>\n\n<\/div>\n\n\t\t\t\t\t\t<\/li>\n\t\t\t\t\t\n\t\t\t\t<\/ul>\n\t\t\t<\/div>\n\n\t\t\n\t\t\t\t\n\t\t<\/div>\n<\/div>\n\n\t\t\t<\/div>\n\t\n"
# }</script>		<script>window.Promise ||
# 			document.write('<script src="https://www.boisestate.edu/spph/wp-content/themes/core/js/vendor/es6-promise.auto.js"><\/script>');
# 		</script>
# 		<script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/themes/core/js/dist/manifest.min.js?ver=1.16.02.06.2025" id="core-webpack-manifest-js"></script>
# <script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/themes/core/js/dist/vendor.min.js?ver=1.16.02.06.2025" id="core-webpack-vendors-js"></script>
# <script type="text/javascript" src="//customer.cludo.com/scripts/bundles/search-script.min.js?ver=3" id="core-cludo-js"></script>
# <script type="text/javascript" id="core-theme-scripts-js-extra">
# /* <![CDATA[ */
# var modern_tribe_i18n = {"nav":{"triggers":{"label_prepend":"Show","label_append":"Navigation","label_return":"Return to previous menu.","label_primary":"Primary","label_section":"Main","label_utility":"Utility"},"sections":{"heading_primary":"Boise State Primary Menu","heading_secondary":"Boise State Secondary Menu","label_primary":"Site Navigation","label_section":"Section Navigation","label_utility":"Utility Site Navigation"},"mobile":{"aria_label":"Primary Navigation"}},"help_text":{"msg_limit":"There is a limit to the messages you can post."},"tooltips":{"add_to_save":"Add Photo to Saved Items","in_this_photo":"Products in this photo"}};
# var modern_tribe_config = {"images_url":"https:\/\/www.boisestate.edu\/spph\/wp-content\/themes\/core\/img\/theme","template_url":"https:\/\/www.boisestate.edu\/spph\/wp-content\/themes\/core\/","menu_locations":{"primary":"global_nav","section_nav":"sections_nav","utility":"utility_nav","sections_nav_flat":"sections_nav_flat"},"off_canvas_items":{"global_nav":{"menu_items":[{"label":"Apply","classes":" primary__list-item primary__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/","class":"site-nav__action primary__action primary__action--depth-0","menu_id":1253,"has_children":false,"meta":[]},{"label":"Visit","classes":" primary__list-item primary__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/","class":"site-nav__action primary__action primary__action--depth-0","menu_id":1252,"has_children":false,"meta":[]},{"label":"Give","classes":" primary__list-item primary__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/giving\/","class":"site-nav__action primary__action primary__action--depth-0","menu_id":1988,"has_children":false,"meta":[]}]},"utility_nav":{"menu_items":[{"label":"myBoiseState","classes":" utility__list-item utility__list-item--depth-0","url":"https:\/\/my.boisestate.edu\/","class":"site-nav__action utility__action utility__action--depth-0","menu_id":1676,"has_children":false,"meta":[]},{"label":"Directory","classes":" utility__list-item utility__list-item--depth-0","url":"https:\/\/directory.boisestate.edu\/","class":"site-nav__action utility__action utility__action--depth-0","menu_id":314,"has_children":false,"meta":[]},{"label":"A-Z Index","classes":" utility__list-item utility__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/index\/","class":"site-nav__action utility__action utility__action--depth-0","menu_id":1752,"has_children":false,"meta":[]},{"label":"Map","classes":" utility__list-item utility__list-item--depth-0","url":"https:\/\/maps.boisestate.edu\/","class":"site-nav__action utility__action utility__action--depth-0","menu_id":316,"has_children":false,"meta":[]},{"label":"News","classes":" utility__list-item utility__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/news\/","class":"site-nav__action utility__action utility__action--depth-0","menu_id":317,"has_children":false,"meta":[]},{"label":"Events","classes":" utility__list-item utility__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/events","class":"site-nav__action utility__action utility__action--depth-0","menu_id":318,"has_children":false,"meta":[]}]},"sections_nav":{"menu_items":[{"label":"School of Public and Population Health","classes":" section_nav__list-item section_nav__list-item--depth-0 section_nav__list-item--hidden-desktop","url":"https:\/\/www.boisestate.edu\/spph","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":999,"has_children":true,"meta":[],"site_id":99,"menu_items":[{"label":"Undergraduate Degrees","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":342,"has_children":true,"menu_items":[{"label":"BS in Health Studies","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/health-studies\/","class":"site-nav__action main__action main__action--depth-1","menu_id":432,"has_children":false,"meta":[]},{"label":"BS in Health Data Analytics","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/health-data-analytics\/","class":"site-nav__action main__action main__action--depth-1","menu_id":26787,"has_children":false,"meta":[]},{"label":"SPPH Certificates","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/minors-and-certificates\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21663,"has_children":false,"meta":[]},{"label":"Accelerated Master of Public Health","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/accelerated-master-of-public-health\/","class":"site-nav__action main__action main__action--depth-1","menu_id":28585,"has_children":false,"meta":[]}],"meta":[]},{"label":"Master of Public Health","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/mph\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":20253,"has_children":true,"menu_items":[{"label":"MPH Student Handbook","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/mhs-handbook\/","class":"site-nav__action main__action main__action--depth-1","menu_id":23741,"has_children":false,"meta":[]},{"label":"Frequently Asked MPH Questions","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/master-of-public-health\/","class":"site-nav__action main__action main__action--depth-1","menu_id":23434,"has_children":false,"meta":[]},{"label":"MPH Emphasis Areas","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/mph-emphasis-areas-2\/","class":"site-nav__action main__action main__action--depth-1","menu_id":28908,"has_children":false,"meta":[]},{"label":"MPH Certificates","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/certificates\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21625,"has_children":false,"meta":[]},{"label":"How do I apply?","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/applying\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21482,"has_children":false,"meta":[]},{"label":"Costs, Financial Aid and Scholarships","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/funding\/","class":"site-nav__action main__action main__action--depth-1","menu_id":23125,"has_children":false,"meta":[]},{"label":"GradWell","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/broncofit\/gradwell\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21875,"has_children":false,"meta":[]},{"label":"Accelerated Master of Public Health","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/accelerated-master-of-public-health\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27212,"has_children":false,"meta":[]},{"label":"Contact","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/contact\/","class":"site-nav__action main__action main__action--depth-1","menu_id":22783,"has_children":false,"meta":[]}],"meta":[]},{"label":"PhD in Public and Population Health Leadership","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/phd\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":25850,"has_children":true,"menu_items":[{"label":"Public and Population Health Leadership PhD Student Handbook","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/public-and-population-health-leadership-phd-student-handbook\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25854,"has_children":false,"meta":[]},{"label":"PhD Curriculum &amp; Plans of Study","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-curriculum-plans-of-study\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25853,"has_children":false,"meta":[]},{"label":"Academic Advising and Mentoring","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-academic-advising-and-mentoring\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25856,"has_children":false,"meta":[]},{"label":"PhD Program Application Requirements","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-admission-requirements\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25858,"has_children":false,"meta":[]},{"label":"Costs, Financial Aid and Scholarships","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-costs-financial-aid-and-scholarships\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25860,"has_children":false,"meta":[]},{"label":"GradWell","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/broncofit\/gradwell\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25861,"has_children":false,"meta":[]},{"label":"Contact","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-contact\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25863,"has_children":false,"meta":[]},{"label":"Current PhD Students","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/pphl-students\/","class":"site-nav__action main__action main__action--depth-1","menu_id":26563,"has_children":false,"meta":[]}],"meta":[]},{"label":"About SPPH","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/spph\/about-spph\/","class":"site-nav__action main__action main__action--depth-0","menu_id":22975,"has_children":false,"meta":[]},{"label":"Faculty and Staff","classes":" main__list-item main__list-item--depth-0 main__list-item--is-current","url":"https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/","class":"site-nav__action main__action main__action--depth-0","menu_id":22673,"has_children":false,"meta":[]},{"label":"Contact SPPH","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/spph\/map-directions\/","class":"site-nav__action main__action main__action--depth-0","menu_id":5352,"has_children":false,"meta":[]},{"label":"Student Resources","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/resources\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":19668,"has_children":true,"menu_items":[{"label":"Internship Opportunities","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/internships\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":21773,"has_children":true,"menu_items":[{"label":"Internship Overview for Students","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/internship-overview-for-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":24954,"has_children":false,"meta":[]},{"label":"Internship Overview for Agencies &amp; Employers","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/info-for-agencies-and-employers\/","class":"site-nav__action main__action main__action--depth-2","menu_id":23167,"has_children":false,"meta":[]},{"label":"SPPH Undergraduate Scholarships","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/internships\/scholarships\/","class":"site-nav__action main__action main__action--depth-2","menu_id":23957,"has_children":false,"meta":[]}],"meta":[]}],"meta":[]},{"label":"SPPH Projects and Initiatives","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":26349,"has_children":true,"menu_items":[{"label":"SPPH Continuing Education Series","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/continuing-education\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27620,"has_children":false,"meta":[]},{"label":"Data Analytics for Statewide Health (DASH) Collaborative","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/dash-data-analytics-for-statewide-health\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":26350,"has_children":true,"menu_items":[{"label":"DASH Lab Student Opportunities","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/dash-data-analytics-for-statewide-health\/student-engagement-opportunities\/","class":"site-nav__action main__action main__action--depth-2","menu_id":26357,"has_children":false,"meta":[]},{"label":"DASH Lab Projects","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/dash-data-analytics-for-statewide-health\/dash-lab-research\/","class":"site-nav__action main__action main__action--depth-2","menu_id":26353,"has_children":false,"meta":[]},{"label":"Community Partner Proposals","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/dash-data-analytics-for-statewide-health\/community-partners\/","class":"site-nav__action main__action main__action--depth-2","menu_id":26441,"has_children":false,"meta":[]},{"label":"Contact","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/dash-data-analytics-for-statewide-health\/contact\/","class":"site-nav__action main__action main__action--depth-2","menu_id":26368,"has_children":false,"meta":[]}],"meta":[]},{"label":"Idaho Caregiver Alliance","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/idaho-caregiver-alliance\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":27420,"has_children":true,"menu_items":[{"label":"ICA Research and Community Projects","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/idaho-caregiver-alliance\/ica-research-and-community-projects\/","class":"site-nav__action main__action main__action--depth-2","menu_id":27453,"has_children":false,"meta":[]},{"label":"Idaho Caregiver Alliance Staff","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/idaho-caregiver-alliance\/idaho-caregiver-alliance-staff\/","class":"site-nav__action main__action main__action--depth-2","menu_id":27421,"has_children":false,"meta":[]}],"meta":[]},{"label":"Center for Excellence in Environmental Health and Safety","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/ceehs\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27454,"has_children":false,"meta":[]},{"label":"Center for Health Policy","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/chp\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27456,"has_children":false,"meta":[]},{"label":"Curl Agricultural Health Lab","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/agriculturalhealth\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27455,"has_children":false,"meta":[]},{"label":"Communities for Youth","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.communitiesforyouth.org\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27457,"has_children":false,"meta":[]}],"meta":[]},{"label":"Alumni and Giving","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/spph\/alumni-and-giving\/","class":"site-nav__action main__action main__action--depth-0","menu_id":25640,"has_children":false,"meta":[]}]},{"label":"About","classes":" section_nav__list-item section_nav__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/about\/","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":4080,"has_children":false,"meta":[]},{"label":"Admissions","classes":" section_nav__list-item section_nav__list-item--depth-0","class":"site-nav__action section_nav__action section_nav__action--depth-0","href":"https:\/\/www.boisestate.edu\/admissions","menu_id":1250,"has_children":true,"meta":[],"site_id":"11","url":"https:\/\/www.boisestate.edu\/admissions","menu_items":[{"label":"Apply","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":15631,"has_children":true,"menu_items":[{"label":"New to College","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/new-to-college\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149605,"has_children":false,"meta":[]},{"label":"Transfer Student","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/transfer\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149608,"has_children":false,"meta":[]},{"label":"Concurrently Enrolled","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/concurrent\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149603,"has_children":false,"meta":[]},{"label":"Returning Boise State Student","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/returning\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149604,"has_children":false,"meta":[]},{"label":"Nondegree Student","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/nondegree\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149606,"has_children":false,"meta":[]},{"label":"Second Bachelor\u2019s Degree","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/secondbachelor\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149607,"has_children":false,"meta":[]},{"label":"Adult Learner","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/adult\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149602,"has_children":false,"meta":[]}],"meta":[]},{"label":"Visit","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":149628,"has_children":true,"menu_items":[{"label":"Campus Tours","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/tours\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164790,"has_children":false,"meta":[]},{"label":"Virtual Visits, Info Sessions, and Appointments","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/virtual-visits\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164407,"has_children":false,"meta":[]},{"label":"Admissions Events","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/special-events\/","class":"site-nav__action main__action main__action--depth-1","menu_id":167034,"has_children":false,"meta":[]},{"label":"Multicultural Events","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/multicultural-events\/","class":"site-nav__action main__action main__action--depth-1","menu_id":165385,"has_children":false,"meta":[]},{"label":"Discover Boise State","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/discover\/","class":"site-nav__action main__action main__action--depth-1","menu_id":162860,"has_children":false,"meta":[]},{"label":"Bronco Day","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":163722,"has_children":true,"menu_items":[{"label":"Bronco Day Home","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/","class":"site-nav__action main__action main__action--depth-2","menu_id":170173,"has_children":false,"meta":[]},{"label":"Register for Bronco Day","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/registration\/","class":"site-nav__action main__action main__action--depth-2","menu_id":168509,"has_children":false,"meta":[]},{"label":"Bronco Day Schedule","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/bronco-day-schedule\/","class":"site-nav__action main__action main__action--depth-2","menu_id":168510,"has_children":false,"meta":[]}],"meta":[]},{"label":"Self-Guided Tour","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/self-guided-tour\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164386,"has_children":false,"meta":[]},{"label":"Plan your visit to Boise State","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/plan-your-visit-to-boise-state\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168508,"has_children":false,"meta":[]}],"meta":[]},{"label":"Student Life","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/studentlife\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":164160,"has_children":true,"menu_items":[{"label":"Find Your Community","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/studentlife\/diversity\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149658,"has_children":false,"meta":[]},{"label":"Welcome to Boise, Idaho","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/studentlife\/welcome-to-boise-idaho\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164270,"has_children":false,"meta":[]}],"meta":[]},{"label":"Explore Academics","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/explore-academics\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":148392,"has_children":true,"menu_items":[{"label":"Major Finder","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/majors.boisestate.edu\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168511,"has_children":false,"meta":[]},{"label":"Blue Turf Thinkers Wanted.","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/blue-turf-thinkers-wanted\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168507,"has_children":false,"meta":[]}],"meta":[]},{"label":"Cost, Aid and Value","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":165939,"has_children":true,"menu_items":[{"label":"Automatic Scholarships for Idaho Residents","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/resident-scholarships\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166788,"has_children":false,"meta":[]},{"label":"Automatic Scholarships for Nonresidents","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/nonresident-scholarships\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166789,"has_children":false,"meta":[]},{"label":"Cost of Attendance","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/cost-of-attendance\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166785,"has_children":false,"meta":[]},{"label":"It Pays to Go to Boise State","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/it-pays\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166786,"has_children":false,"meta":[]}],"meta":[]},{"label":"Next Steps","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":166660,"has_children":true,"menu_items":[{"label":"Next Steps for Admitted First Year Students","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":166661,"has_children":true,"menu_items":[{"label":"Step 1: Set up Your MyBoiseState Account","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-1-set-up-your-myboisestate-account\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166667,"has_children":false,"meta":[]},{"label":"Step 2: Review Scholarship and Financial Aid Opportunities","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-2-review-scholarship-and-financial-aid-opportunities\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166666,"has_children":false,"meta":[]},{"label":"Step 3: Complete Your Intent to Enroll","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-3-complete-your-intent-to-enroll\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166665,"has_children":false,"meta":[]},{"label":"Step 4: Apply for On-Campus Housing","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-4-apply-for-on-campus-housing\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166664,"has_children":false,"meta":[]},{"label":"Step 5: Register for Orientation","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-5-register-for-orientation\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166663,"has_children":false,"meta":[]},{"label":"Step 6: Send Your Final Transcripts","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-6-send-your-final-transcripts\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166662,"has_children":false,"meta":[]}],"meta":[]},{"label":"Next Steps for Admitted Transfer Students","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":166790,"has_children":true,"menu_items":[{"label":"Step 1: Set up Your MyBoiseState Account","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-1-set-up-your-myboisestate-account-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167132,"has_children":false,"meta":[]},{"label":"Step 2: Review Scholarship and Financial Aid Opportunities","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-2-review-scholarship-and-financial-aid-opportunities-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167131,"has_children":false,"meta":[]},{"label":"Step 3: Complete Your Intent to Enroll","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-3-complete-your-intent-to-enroll-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167130,"has_children":false,"meta":[]},{"label":"Step 4: Apply for On-Campus Housing","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-4-apply-for-on-campus-housing-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167129,"has_children":false,"meta":[]},{"label":"Step 5: Register for Virtual Orientation","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-5-register-for-virtual-orientation-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167128,"has_children":false,"meta":[]},{"label":"Step 6: Send Your Final Transcripts","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-6-send-your-final-transcripts-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167127,"has_children":false,"meta":[]}],"meta":[]},{"label":"Next Steps for Admitted Non-Traditional Students","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/non-traditional\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166791,"has_children":false,"meta":[]},{"label":"Intent to Enroll","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/intenttoenroll\/","class":"site-nav__action main__action main__action--depth-1","menu_id":134202,"has_children":false,"meta":[]}],"meta":[]},{"label":"Connect with Us!","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":148389,"has_children":true,"menu_items":[{"label":"Request Information","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/request-information\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166792,"has_children":false,"meta":[]},{"label":"Admissions Staff","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/staff\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164271,"has_children":false,"meta":[]},{"label":"High School Counselor Resources","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/counselor\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168501,"has_children":false,"meta":[]},{"label":"Transfer Advisor Resources","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/transfer\/advisor-resources\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168502,"has_children":false,"meta":[]},{"label":"Follow Us on Social Media","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/follow-us\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166793,"has_children":false,"meta":[]}],"meta":[]},{"label":"FAQ","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/admissions\/frequently-asked-questions\/","class":"site-nav__action main__action main__action--depth-0","menu_id":165421,"has_children":false,"meta":[]}]},{"label":"Academics","classes":" section_nav__list-item section_nav__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/academics-landing\/","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":643,"has_children":false,"meta":[]},{"label":"Research","classes":" section_nav__list-item section_nav__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/research\/","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":312,"has_children":false,"meta":[]}]},"sections_nav_flat":[{"depth":0,"menu_items":[{"label":"School of Public and Population Health","classes":" section_nav__list-item section_nav__list-item--depth-0 section_nav__list-item--hidden-desktop","url":"https:\/\/www.boisestate.edu\/spph","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":999,"has_children":true,"meta":[],"site_id":99,"child_id":"menu-top","parent_id":"menu-top"},{"label":"About","classes":" section_nav__list-item section_nav__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/about\/","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":4080,"has_children":false,"meta":[],"child_id":"menu-top"},{"label":"Admissions","classes":" section_nav__list-item section_nav__list-item--depth-0","class":"site-nav__action section_nav__action section_nav__action--depth-0","href":"https:\/\/www.boisestate.edu\/admissions","menu_id":1250,"has_children":true,"meta":[],"site_id":"11","url":"https:\/\/www.boisestate.edu\/admissions","child_id":"menu-top","parent_id":"menu-top"},{"label":"Academics","classes":" section_nav__list-item section_nav__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/academics-landing\/","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":643,"has_children":false,"meta":[],"child_id":"menu-top"},{"label":"Research","classes":" section_nav__list-item section_nav__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/research\/","class":"site-nav__action section_nav__action section_nav__action--depth-0","menu_id":312,"has_children":false,"meta":[],"child_id":"menu-top"}],"menu_id":"menu-top","parent_id":false,"label":""},{"depth":1,"menu_items":[{"label":"Undergraduate Degrees","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":342,"has_children":true,"meta":[],"child_id":999,"parent_id":999},{"label":"Master of Public Health","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/mph\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":20253,"has_children":true,"meta":[],"child_id":999,"parent_id":999},{"label":"PhD in Public and Population Health Leadership","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/phd\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":25850,"has_children":true,"meta":[],"child_id":999,"parent_id":999},{"label":"About SPPH","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/spph\/about-spph\/","class":"site-nav__action main__action main__action--depth-0","menu_id":22975,"has_children":false,"meta":[],"child_id":999},{"label":"Faculty and Staff","classes":" main__list-item main__list-item--depth-0 main__list-item--is-current","url":"https:\/\/www.boisestate.edu\/spph\/faculty-and-staff-directory\/","class":"site-nav__action main__action main__action--depth-0","menu_id":22673,"has_children":false,"meta":[],"child_id":999},{"label":"Contact SPPH","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/spph\/map-directions\/","class":"site-nav__action main__action main__action--depth-0","menu_id":5352,"has_children":false,"meta":[],"child_id":999},{"label":"Student Resources","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/resources\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":19668,"has_children":true,"meta":[],"child_id":999,"parent_id":999},{"label":"SPPH Projects and Initiatives","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":26349,"has_children":true,"meta":[],"child_id":999,"parent_id":999},{"label":"Alumni and Giving","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/spph\/alumni-and-giving\/","class":"site-nav__action main__action main__action--depth-0","menu_id":25640,"has_children":false,"meta":[],"child_id":999}],"menu_id":999,"parent_id":"menu-top","label":"School of Public and Population Health"},{"depth":1,"menu_items":[{"label":"Apply","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":15631,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"Visit","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":149628,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"Student Life","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/studentlife\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":164160,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"Explore Academics","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/explore-academics\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":148392,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"Cost, Aid and Value","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":165939,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"Next Steps","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":166660,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"Connect with Us!","classes":" main__list-item main__list-item--depth-0 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/","class":"site-nav__action main__action main__action--depth-0 main__action--has-children","menu_id":148389,"has_children":true,"meta":[],"child_id":1250,"parent_id":1250},{"label":"FAQ","classes":" main__list-item main__list-item--depth-0","url":"https:\/\/www.boisestate.edu\/admissions\/frequently-asked-questions\/","class":"site-nav__action main__action main__action--depth-0","menu_id":165421,"has_children":false,"meta":[],"child_id":1250}],"menu_id":1250,"parent_id":"menu-top","label":"Admissions"},{"depth":2,"menu_items":[{"label":"BS in Health Studies","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/health-studies\/","class":"site-nav__action main__action main__action--depth-1","menu_id":432,"has_children":false,"meta":[],"child_id":342},{"label":"BS in Health Data Analytics","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/health-data-analytics\/","class":"site-nav__action main__action main__action--depth-1","menu_id":26787,"has_children":false,"meta":[],"child_id":342},{"label":"SPPH Certificates","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/undergraduate\/minors-and-certificates\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21663,"has_children":false,"meta":[],"child_id":342},{"label":"Accelerated Master of Public Health","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/accelerated-master-of-public-health\/","class":"site-nav__action main__action main__action--depth-1","menu_id":28585,"has_children":false,"meta":[],"child_id":342}],"menu_id":342,"parent_id":999,"label":"Undergraduate Degrees"},{"depth":2,"menu_items":[{"label":"MPH Student Handbook","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/mhs-handbook\/","class":"site-nav__action main__action main__action--depth-1","menu_id":23741,"has_children":false,"meta":[],"child_id":20253},{"label":"Frequently Asked MPH Questions","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/master-of-public-health\/","class":"site-nav__action main__action main__action--depth-1","menu_id":23434,"has_children":false,"meta":[],"child_id":20253},{"label":"MPH Emphasis Areas","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/mph-emphasis-areas-2\/","class":"site-nav__action main__action main__action--depth-1","menu_id":28908,"has_children":false,"meta":[],"child_id":20253},{"label":"MPH Certificates","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/certificates\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21625,"has_children":false,"meta":[],"child_id":20253},{"label":"How do I apply?","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/applying\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21482,"has_children":false,"meta":[],"child_id":20253},{"label":"Costs, Financial Aid and Scholarships","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/funding\/","class":"site-nav__action main__action main__action--depth-1","menu_id":23125,"has_children":false,"meta":[],"child_id":20253},{"label":"GradWell","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/broncofit\/gradwell\/","class":"site-nav__action main__action main__action--depth-1","menu_id":21875,"has_children":false,"meta":[],"child_id":20253},{"label":"Accelerated Master of Public Health","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/accelerated-master-of-public-health\/","class":"site-nav__action main__action main__action--depth-1","menu_id":27212,"has_children":false,"meta":[],"child_id":20253},{"label":"Contact","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/mph\/contact\/","class":"site-nav__action main__action main__action--depth-1","menu_id":22783,"has_children":false,"meta":[],"child_id":20253}],"menu_id":20253,"parent_id":999,"label":"Master of Public Health"},{"depth":2,"menu_items":[{"label":"Public and Population Health Leadership PhD Student Handbook","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/public-and-population-health-leadership-phd-student-handbook\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25854,"has_children":false,"meta":[],"child_id":25850},{"label":"PhD Curriculum &amp; Plans of Study","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-curriculum-plans-of-study\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25853,"has_children":false,"meta":[],"child_id":25850},{"label":"Academic Advising and Mentoring","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-academic-advising-and-mentoring\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25856,"has_children":false,"meta":[],"child_id":25850},{"label":"PhD Program Application Requirements","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-admission-requirements\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25858,"has_children":false,"meta":[],"child_id":25850},{"label":"Costs, Financial Aid and Scholarships","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-costs-financial-aid-and-scholarships\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25860,"has_children":false,"meta":[],"child_id":25850},{"label":"GradWell","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/broncofit\/gradwell\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25861,"has_children":false,"meta":[],"child_id":25850},{"label":"Contact","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/phd-contact\/","class":"site-nav__action main__action main__action--depth-1","menu_id":25863,"has_children":false,"meta":[],"child_id":25850},{"label":"Current PhD Students","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/spph\/phd\/pphl-students\/","class":"site-nav__action main__action main__action--depth-1","menu_id":26563,"has_children":false,"meta":[],"child_id":25850}],"menu_id":25850,"parent_id":999,"label":"PhD in Public and Population Health Leadership"},{"depth":2,"menu_items":[{"label":"New to College","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/new-to-college\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149605,"has_children":false,"meta":[],"child_id":15631},{"label":"Transfer Student","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/transfer\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149608,"has_children":false,"meta":[],"child_id":15631},{"label":"Concurrently Enrolled","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/concurrent\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149603,"has_children":false,"meta":[],"child_id":15631},{"label":"Returning Boise State Student","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/returning\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149604,"has_children":false,"meta":[],"child_id":15631},{"label":"Nondegree Student","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/nondegree\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149606,"has_children":false,"meta":[],"child_id":15631},{"label":"Second Bachelor\u2019s Degree","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/secondbachelor\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149607,"has_children":false,"meta":[],"child_id":15631},{"label":"Adult Learner","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/apply\/adult\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149602,"has_children":false,"meta":[],"child_id":15631}],"menu_id":15631,"parent_id":1250,"label":"Apply"},{"depth":2,"menu_items":[{"label":"Internship Opportunities","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/spph\/internships\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":21773,"has_children":true,"meta":[],"child_id":19668,"parent_id":19668}],"menu_id":19668,"parent_id":999,"label":"Student Resources"},{"depth":2,"menu_items":[{"label":"Campus Tours","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/tours\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164790,"has_children":false,"meta":[],"child_id":149628},{"label":"Virtual Visits, Info Sessions, and Appointments","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/virtual-visits\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164407,"has_children":false,"meta":[],"child_id":149628},{"label":"Admissions Events","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/special-events\/","class":"site-nav__action main__action main__action--depth-1","menu_id":167034,"has_children":false,"meta":[],"child_id":149628},{"label":"Multicultural Events","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/multicultural-events\/","class":"site-nav__action main__action main__action--depth-1","menu_id":165385,"has_children":false,"meta":[],"child_id":149628},{"label":"Discover Boise State","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/discover\/","class":"site-nav__action main__action main__action--depth-1","menu_id":162860,"has_children":false,"meta":[],"child_id":149628},{"label":"Bronco Day","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":163722,"has_children":true,"meta":[],"child_id":149628,"parent_id":149628},{"label":"Self-Guided Tour","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/self-guided-tour\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164386,"has_children":false,"meta":[],"child_id":149628},{"label":"Plan your visit to Boise State","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/plan-your-visit-to-boise-state\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168508,"has_children":false,"meta":[],"child_id":149628}],"menu_id":149628,"parent_id":1250,"label":"Visit"},{"depth":2,"menu_items":[{"label":"Find Your Community","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/studentlife\/diversity\/","class":"site-nav__action main__action main__action--depth-1","menu_id":149658,"has_children":false,"meta":[],"child_id":164160},{"label":"Welcome to Boise, Idaho","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/studentlife\/welcome-to-boise-idaho\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164270,"has_children":false,"meta":[],"child_id":164160}],"menu_id":164160,"parent_id":1250,"label":"Student Life"},{"depth":2,"menu_items":[{"label":"Major Finder","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/majors.boisestate.edu\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168511,"has_children":false,"meta":[],"child_id":148392},{"label":"Blue Turf Thinkers Wanted.","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/blue-turf-thinkers-wanted\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168507,"has_children":false,"meta":[],"child_id":148392}],"menu_id":148392,"parent_id":1250,"label":"Explore Academics"},{"depth":2,"menu_items":[{"label":"Automatic Scholarships for Idaho Residents","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/resident-scholarships\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166788,"has_children":false,"meta":[],"child_id":165939},{"label":"Automatic Scholarships for Nonresidents","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/nonresident-scholarships\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166789,"has_children":false,"meta":[],"child_id":165939},{"label":"Cost of Attendance","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/cost-of-attendance\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166785,"has_children":false,"meta":[],"child_id":165939},{"label":"It Pays to Go to Boise State","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/cost-aid-value\/it-pays\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166786,"has_children":false,"meta":[],"child_id":165939}],"menu_id":165939,"parent_id":1250,"label":"Cost, Aid and Value"},{"depth":2,"menu_items":[{"label":"Next Steps for Admitted First Year Students","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":166661,"has_children":true,"meta":[],"child_id":166660,"parent_id":166660},{"label":"Next Steps for Admitted Transfer Students","classes":" main__list-item main__list-item--depth-1 main__list-item--has-children","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/","class":"site-nav__action main__action main__action--depth-1 main__action--has-children","menu_id":166790,"has_children":true,"meta":[],"child_id":166660,"parent_id":166660},{"label":"Next Steps for Admitted Non-Traditional Students","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/non-traditional\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166791,"has_children":false,"meta":[],"child_id":166660},{"label":"Intent to Enroll","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/intenttoenroll\/","class":"site-nav__action main__action main__action--depth-1","menu_id":134202,"has_children":false,"meta":[],"child_id":166660}],"menu_id":166660,"parent_id":1250,"label":"Next Steps"},{"depth":2,"menu_items":[{"label":"Request Information","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/request-information\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166792,"has_children":false,"meta":[],"child_id":148389},{"label":"Admissions Staff","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/staff\/","class":"site-nav__action main__action main__action--depth-1","menu_id":164271,"has_children":false,"meta":[],"child_id":148389},{"label":"High School Counselor Resources","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/counselor\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168501,"has_children":false,"meta":[],"child_id":148389},{"label":"Transfer Advisor Resources","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/transfer\/advisor-resources\/","class":"site-nav__action main__action main__action--depth-1","menu_id":168502,"has_children":false,"meta":[],"child_id":148389},{"label":"Follow Us on Social Media","classes":" main__list-item main__list-item--depth-1","url":"https:\/\/www.boisestate.edu\/admissions\/connect\/follow-us\/","class":"site-nav__action main__action main__action--depth-1","menu_id":166793,"has_children":false,"meta":[],"child_id":148389}],"menu_id":148389,"parent_id":1250,"label":"Connect with Us!"},{"depth":3,"menu_items":[{"label":"Internship Overview for Students","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/internship-overview-for-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":24954,"has_children":false,"meta":[],"child_id":21773},{"label":"Internship Overview for Agencies &amp; Employers","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/info-for-agencies-and-employers\/","class":"site-nav__action main__action main__action--depth-2","menu_id":23167,"has_children":false,"meta":[],"child_id":21773},{"label":"SPPH Undergraduate Scholarships","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/internships\/scholarships\/","class":"site-nav__action main__action main__action--depth-2","menu_id":23957,"has_children":false,"meta":[],"child_id":21773}],"menu_id":21773,"parent_id":19668,"label":"Internship Opportunities"},{"depth":3,"menu_items":[{"label":"Bronco Day Home","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/","class":"site-nav__action main__action main__action--depth-2","menu_id":170173,"has_children":false,"meta":[],"child_id":163722},{"label":"Register for Bronco Day","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/registration\/","class":"site-nav__action main__action main__action--depth-2","menu_id":168509,"has_children":false,"meta":[],"child_id":163722},{"label":"Bronco Day Schedule","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/visit\/broncoday\/bronco-day-schedule\/","class":"site-nav__action main__action main__action--depth-2","menu_id":168510,"has_children":false,"meta":[],"child_id":163722}],"menu_id":163722,"parent_id":149628,"label":"Bronco Day"},{"depth":3,"menu_items":[{"label":"ICA Research and Community Projects","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/idaho-caregiver-alliance\/ica-research-and-community-projects\/","class":"site-nav__action main__action main__action--depth-2","menu_id":27453,"has_children":false,"meta":[],"child_id":27420},{"label":"Idaho Caregiver Alliance Staff","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/spph\/spph-projects-and-initiatives\/idaho-caregiver-alliance\/idaho-caregiver-alliance-staff\/","class":"site-nav__action main__action main__action--depth-2","menu_id":27421,"has_children":false,"meta":[],"child_id":27420}],"menu_id":27420,"parent_id":26349,"label":"Idaho Caregiver Alliance"},{"depth":3,"menu_items":[{"label":"Step 1: Set up Your MyBoiseState Account","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-1-set-up-your-myboisestate-account\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166667,"has_children":false,"meta":[],"child_id":166661},{"label":"Step 2: Review Scholarship and Financial Aid Opportunities","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-2-review-scholarship-and-financial-aid-opportunities\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166666,"has_children":false,"meta":[],"child_id":166661},{"label":"Step 3: Complete Your Intent to Enroll","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-3-complete-your-intent-to-enroll\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166665,"has_children":false,"meta":[],"child_id":166661},{"label":"Step 4: Apply for On-Campus Housing","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-4-apply-for-on-campus-housing\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166664,"has_children":false,"meta":[],"child_id":166661},{"label":"Step 5: Register for Orientation","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-5-register-for-orientation\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166663,"has_children":false,"meta":[],"child_id":166661},{"label":"Step 6: Send Your Final Transcripts","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/first-year\/step-6-send-your-final-transcripts\/","class":"site-nav__action main__action main__action--depth-2","menu_id":166662,"has_children":false,"meta":[],"child_id":166661}],"menu_id":166661,"parent_id":166660,"label":"Next Steps for Admitted First Year Students"},{"depth":3,"menu_items":[{"label":"Step 1: Set up Your MyBoiseState Account","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-1-set-up-your-myboisestate-account-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167132,"has_children":false,"meta":[],"child_id":166790},{"label":"Step 2: Review Scholarship and Financial Aid Opportunities","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-2-review-scholarship-and-financial-aid-opportunities-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167131,"has_children":false,"meta":[],"child_id":166790},{"label":"Step 3: Complete Your Intent to Enroll","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-3-complete-your-intent-to-enroll-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167130,"has_children":false,"meta":[],"child_id":166790},{"label":"Step 4: Apply for On-Campus Housing","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-4-apply-for-on-campus-housing-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167129,"has_children":false,"meta":[],"child_id":166790},{"label":"Step 5: Register for Virtual Orientation","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-5-register-for-virtual-orientation-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167128,"has_children":false,"meta":[],"child_id":166790},{"label":"Step 6: Send Your Final Transcripts","classes":" main__list-item main__list-item--depth-2","url":"https:\/\/www.boisestate.edu\/admissions\/nextsteps\/transfer\/step-6-send-your-final-transcripts-transfer-students\/","class":"site-nav__action main__action main__action--depth-2","menu_id":167127,"has_children":false,"meta":[],"child_id":166790}],"menu_id":166790,"parent_id":166660,"label":"Next Steps for Admitted Transfer Students"}]},"current_active_site":"99","current_active_menu_id":"999","current_active_top_level_menu_id":"999"};
# /* ]]> */
# </script>
# <script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/themes/core/js/dist/scripts.min.js?ver=1.16.02.06.2025" id="core-theme-scripts-js"></script>
# <script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/themes/core/js/vendor/jquery.waypoints.min.js?ver=1.16.02.06.2025" id="core-theme-waypoints-js"></script>
# <script type="text/javascript" src="https://www.boisestate.edu/spph/wp-content/themes/core/js/vendor/sticky.min.js?ver=1.16.02.06.2025" id="core-theme-waypoints-sticky-js"></script>

# <!-- Hand crafted by Modern Tribe, Inc. (http://tri.be) -->



# <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"NRJS-2c42fcd46722616451c","applicationID":"1302301515","transactionName":"ZVxUbEdQXBEFWkNaXlwWd1tBWF0MS0lWVFQ=","queueTime":0,"applicationTime":675,"atts":"SRtXGg9KTx8=","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
# </html>


# <!-- plugin=object-cache-pro client=phpredis metric#hits=5542 metric#misses=279 metric#hit-ratio=95.2 metric#bytes=3277358 metric#prefetches=373 metric#store-reads=205 metric#store-writes=10 metric#store-hits=524 metric#store-misses=273 metric#sql-queries=3 metric#ms-total=656.23 metric#ms-cache=239.75 metric#ms-cache-avg=1.1203 metric#ms-cache-ratio=36.5 -->
# """


html = """
    
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <meta name="author" content="" />
    <title>Aabhyasa || Leading in webinar providers</title>
    <base href="https://aabhyasa.com/">
<!-- Favicon-->
<link rel="icon" href="images/aabhyasa_logo_element.png" type="image/x-icon">


<!-- Bootstrap 5 CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<!-- Font Awesome CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">


<!-- custom files link  -->
<link rel="stylesheet" href="assets/css/style.css">
<link rel="stylesheet" href="assets/css/responsive.css">

<!-- owl carousel css  -->
<link rel="stylesheet" href="assets/css/owl.carousel.css">
<link rel="stylesheet" href="assets/css/owl.carousel.min.css">
<!-- Sweet Alert -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.all.min.js"></script>
</head>

<body>

    <!-- Navbar content  -->
<div class="top-header py-3">
    <div class="container-fluid d-flex justify-content-between text-black">
        <div class="social-contact">
            <a href="mailto:info@aabhyasa.com">
                <i class="fa-solid fa-envelope"></i>
                <span class="d-none d-md-inline-block">info@aabhyasa.com</span>
            </a>
            <!--<a href="#" class="ms-3">-->
            <!--    <i class="fa-solid fa-phone"></i>-->
            <!--    <span class="d-none d-md-inline-block"> +1 234 4567 8910</span>-->
            <!--</a>-->
        </div>
        <div >
            <p class="tagline">Innovative and Diversified Professional Webinar
            </p>
        </div>

    </div>
</div>

</div>
<header>
    <div class="container-fluid">
        <a href="index" class="logo">
            <img src="images/aabhyasa_logo_element.png" alt="" class="img-fluid">aabhyasa
        </a>
        <nav class="navigation">
            <ul>
                <li><a href="index">Home</a></li>
                <li><a href="about">About</a></li>
                <li><a href="services">Services</a></li>
                <li><a href="team">Team</a></li>
                <li><a href="career">Career</a></li>
                <li><a href="contact">Contact</a></li>

            </ul>
        </nav>
        <div class="menuToggle" onclick="ToggleMenu();"><i class="fa-solid fa-bars-staggered"></i></div>
    </div>
</header>        
    <!-- carousel home start -->
    <section class="home-header">
        <div id="home_carousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <!-- <div class="gradient"></div> -->
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="images/carousel-banner/banner3.jpg" class="d-block w-100" alt="...">
                    <div class="carousel-caption">
                        <h1 class="slide-up">Innovative Learning Solutions</h1>
                        <h5 class="slide-up">Innovatively, our webinar platform upholds trust, confidence, and determination—ensuring excellence within a compact timeframe.</h5>
                        <div class="mt-5 slide-up">
                            <a href="/contact" class="main-btn me-2">Contact us <i class="fa-solid fa-chevron-right"></i></a>
                            <a href="/about" class="fill-btn">Read more <i class="fa-solid fa-chevron-right"></i></a>
                        </div>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="images/carousel-banner/banner2.jpg" class="d-block w-100" alt="...">
                    <div class="carousel-caption">
                        <h1 class="slide-up">Innovative Learning Solutions</h1>
                        <h5 class="slide-up">Innovatively, our webinar platform upholds trust, confidence, and determination—ensuring excellence within a compact timeframe.</h5>
                        <div class="mt-5 slide-up">
                            <a href="/contact" class="main-btn me-2">Contact us <i class="fa-solid fa-chevron-right"></i></a>
                            <a href="/about" class="fill-btn">Read more <i class="fa-solid fa-chevron-right"></i></a>
                        </div>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="images/carousel-banner/banner1.jpg" class="d-block w-100" alt="...">
                    <div class="carousel-caption">
                        <h1 class="slide-up">Innovative Learning Solutions</h1>
                        <h5 class="slide-up">Innovatively, our webinar platform upholds trust, confidence, and determination—ensuring excellence within a compact timeframe.</h5>
                        <div class="mt-5 slide-up">
                            <a href="/contact" class="main-btn me-2">Contact us <i class="fa-solid fa-chevron-right"></i></a>
                            <a href="/about" class="fill-btn">Read more <i class="fa-solid fa-chevron-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#home_carousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#home_carousel" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </section>
    <!-- carousel home end -->


    <!-- about and mission section start -->
    <section>
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2>Welcome to <span>Aabhyasa</span></h2>
            </div>
            <div class="row mx-2">
                <div class="col-md-6 col-12 about-div">
                    <div>
                        <h3 class="sub_heading">About Us</h3>
                        <p>
                            Welcome to Aabhyasa, where knowledge meets opportunity! We are your go-to hub for cutting-edge webinars spanning the dynamic worlds of US Healthcare, Medical Coding and Billing, Human Resources, Pharmaceutical, Banking, Finance, and Real Estate. Our mission is simple: to equip you with the insights and updates you need to thrive in today’s fast-paced professional landscape. Imagine a place where industry pioneers gather to share their knowledge, where you can tap into the collective wisdom of experts, and where your career potential can skyrocket. That’s what Aabhyasa is all about.
                        </p>
                        <h3 class="sub_heading">Our Mission</h3>
                        <p>
                        Our mission at Aabhyasa is to empower professionals and organisations by delivering high-quality, relevant, and actionable knowledge through our expertly curated webinars. We strive to bridge the gap between information and implementation, helping you stay ahead in a rapidly evolving world.
                        </p>

                    </div>

                    <div class="my-3">
                        <!-- <a href="#" class="fill-btn">Read more <i class="fa-solid fa-chevron-right"></i></a> -->
                        <img src="images/about-us.png" alt="" class="img-fluid">
                    </div>
                </div>
                <div class="col-md-6 col-12 mission-div">
                    <div>
                        <h3 class="sub_heading">Our Vision</h3>
                        <p>
                        We envision a world where continuous learning and professional development are accessible to all. By providing cutting-edge webinars, we aim to create a community of well-informed, skilled, and proactive professionals who drive innovation and excellence in their fields.
                        </p>


                    </div>
                    <div>
                        <h3 class="sub_heading">Our Goal</h3>
                        <p>
                        At Aabhyasa, our goal is to revolutionise the way professionals gain industry-specific knowledge and skills. We are dedicated to empowering you with cutting-edge insights and practical expertise through our dynamic webinars on US healthcare, medical coding and billing, HR, Pharma, Banking, Finance, and Real Estate. By fostering a culture of continuous learning and innovation, we aim to bridge knowledge gaps and create a vibrant community of experts and learners. Our mission is to transform your professional journey, helping you stay ahead of industry trends and achieve excellence in your field. Join us and experience the power of informed proactive growth.
                        </p>


                    </div>

                    <div class="my-3">
                        <!-- <a href="#" class="fill-btn">Read more <i class="fa-solid fa-chevron-right"></i></a> -->
                        <img src="images/mission.jpg" alt="" class="img-fluid">
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- about and mission section end -->

    <!-- Our organizers sections start -->
    <section class="organizers-section">
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2 class="ms-3">
                    Our Team
                </h2>
            </div>
            <div class="row mx-2 row-gap-5">
                                <div class="col-lg-6 col-12 d-flex flex-md-row flex-column ">
                    <img src="images/team/gopal-yadav.jpg" alt="Gopal Yadav" class="img-fluid rounded-2 mb-3 me-3 w-auto  object-fit-cover" style="max-width: 300px;">
                    <div class="col organizers_details">
                                                    <a class="name" href="team/gopal-yadav" >Mr. Gopal Yadav</a>
                        <p class="title">Director, Aabhyasa</p>
                        <div class="social_links">
                            <a href="https://www.linkedin.com/in/gopal-y-959451208/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                            <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                            <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                        </div>
                        <p class="desc">
                            He has a wealth of experience that spans marketing, webinars, technology, compliance, and every essential business facet. His all-encompassing expertise, from managing technology resources to navigating complex regulatory landscapes, enables the company to flourish in a dynamic market. He sets the strategic direction for Aabhyasa Technologies, focusing on leveraging technology for learning and development. His mantra is "never settle," inspiring his team to strive for continuous improvement and innovation across industries.                        </p>
                        <a href="team/gopal-yadav" class="view-btn fs-6 p-0 fst-italic">
                            Read more
                        </a>
                    </div>
                </div>
                
                <div class="col-lg-6 col-12 d-flex flex-md-row flex-column">
                    <img src="images/team/govind-yadav.jpeg" alt="Govind Yadav" class="img-fluid rounded-2 mb-3 me-3 w-auto  object-fit-cover" style="max-width: 300px;">
                    <div class="col organizers_details">
                                                    <a class="name" href="team/gobind-yadav">Mr. Gobind Yadav</a>
                        <p class="title">Director, Aabhyasa</p>
                        <div class="social_links">
                            <a href="https://www.linkedin.com/in/gobind-yadav-57714964/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                        </div>
                        <p class="desc">
                            He seamlessly orchestrates the company’s overall operations with a sharp focus on strategy, compliance, and data management. With an in-depth knowledge of regulatory standards, payment systems, and management practices, he ensures that every aspect of the business functions smoothly. His forward-thinking approach, combined with his mastery of compliance and operational intricacies, helps the company stay ahead of industry demands. Gobind’s leadership is defined by his unwavering energy and his belief that true success lies in breaking away from the norm, guiding the team to develop action-driven strategies that set them apart from the competition.                        </p>
                        <a href="team/gobind-yadav" class="view-btn fs-6 p-0 fst-italic">
                            Read more
                        </a>
                    </div>
                </div>

                
                
                <div class="col-lg-12">
                    <div class="row">
                                                 <div class="col-lg-4 col-md-6 col-12 mb-5">
                            <div class="row">
                                <div class="col-5">
                                    <div class="member-img">
                                        <img class=" img-fluid" src="images/team/virendra-tiwari.jpeg">
                                    </div>
                                </div>
                                <div class="col organizers_details">
                                                                            <a class="name" href="team/virendra-kumar-tiwari">Mr. Virendra Kumar Tiwari</a>
                                    <p class="title">Assistant Manager Human Resources</p>
                                    <div class="social_links">
                                        <a href="https://linkedin.com/in/virendra-kumar-tiwari-6a487785" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                                        <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                                        <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                                    </div>
                                    <p class="desc">
                                        
                                        Mr. Virendra Kumar Tiwari is a dynamic leader with over a decade of expertise in Human Resources and Operations and  a expert of talent acquisition, retention, and HR compliance, he ...                                    </p>
                                    <a href="team/virendra-kumar-tiwari" class="view-btn fs-6 p-0 fst-italic">
                                        Read more
                                    </a>
                                </div>
                            </div>
                        </div>
                                                
                                                <div class="col-lg-4 col-md-6 col-12 mb-5">
                            <div class="row">
                                <div class="col-5">
                                    <div class="member-img">
                                        <img class=" img-fluid" src="images/team/krishna.jpeg">
                                    </div>
                                </div>
                                <div class="col organizers_details">
                                                                            <a class="name" href="team/krishna-kumar-jaiswal">Mr. Krishna Kumar Jaiswal</a>
                                    <p class="title">Assistant Manager of Accounts & Finance</p>
                                    <div class="social_links">
                                        <a href="https://linkedin.com/in/krishna-kumar-jaiswal-aa88a44a" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                                        <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                                        <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                                    </div>
                                    <p class="desc">
                                        
                                        As Assistant Manager of Accounts & Finance, he expertly navigates the complexities of financial management, budgeting, compliance, and risk mitigation, ensuring the company’s long-term growth. With a solid academic foundation ...                                    </p>
                                    <a href="team/krishna-kumar-jaiswal" class="view-btn fs-6 p-0 fst-italic">
                                        Read more
                                    </a>
                                </div>
                            </div>
                        </div>
                                                
                                                <div class="col-lg-4 col-md-6 col-12 mb-5">
                            <div class="row">
                                <div class="col-5">
                                    <div class="member-img">
                                        <img class=" img-fluid" src="images/team/abhishek.jpeg">
                                    </div>
                                </div>
                                <div class="col organizers_details">
                                                                            <a class="name" href="team/abhishek-jaiswal">Mr. Abhishek Jaiswal</a>
                                    <p class="title">Assistant Manager of   Sales & Marketing</p>
                                    <div class="social_links">
                                        <a href="https://linkedin.com/in/abhishek-jaiswal-29a515125" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                                        <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                                        <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                                    </div>
                                    <p class="desc">
                                        
                                        With a Master’s in Computer Science and 8 years of experience in sales and marketing, primarily in email marketing. He is responsible for crafting innovative marketing strategies, driving major campaign ...                                    </p>
                                    <a href="team/abhishek-jaiswal" class="view-btn fs-6 p-0 fst-italic">
                                        Read more
                                    </a>
                                </div>
                            </div>
                        </div>
                                                
                                                <div class="col-lg-4 col-md-6 col-12 mb-5">
                            <div class="row">
                                <div class="col-5">
                                    <div class="member-img">
                                        <img class=" img-fluid" src="images/team/jai-prakash.jpeg">
                                    </div>
                                </div>
                                <div class="col organizers_details">
                                                                            <a class="name" href="team/jai-prakash-maurya">Mr. Jai Prakash Maurya</a>
                                    <p class="title">Team Lead Web Application Development</p>
                                    <div class="social_links">
                                        <a href="https://linkedin.com/in/jai-prakash-m-2857711a0" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                                        <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                                        <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                                    </div>
                                    <p class="desc">
                                        
                                        He is a visionary leader in Web Application Development, with over nine years of experience crafting custom solutions that push the boundaries of innovation. Holding a bachelor’s degree in ...                                    </p>
                                    <a href="team/jai-prakash-maurya" class="view-btn fs-6 p-0 fst-italic">
                                        Read more
                                    </a>
                                </div>
                            </div>
                        </div>
                                                
                                                <div class="col-lg-4 col-md-6 col-12 mb-5">
                            <div class="row">
                                <div class="col-5">
                                    <div class="member-img">
                                        <img class=" img-fluid" src="images/team/prerna-tiwari.jpeg">
                                    </div>
                                </div>
                                <div class="col organizers_details">
                                                                            <a class="name" href="team/prerna-tiwari">Ms. Prerna Tiwari</a>
                                    <p class="title">Team Lead of Operations</p>
                                    <div class="social_links">
                                        <a href="https://linkedin.com/in/prerna-tiwari-a73109301" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                                        <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                                        <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                                    </div>
                                    <p class="desc">
                                        
                                        Rising through the ranks from a Process Associate to Team Lead of Operations, she now oversees the entire operational framework, ensuring seamless project management, timely execution, and customer satisfaction. Her ...                                    </p>
                                    <a href="team/prerna-tiwari" class="view-btn fs-6 p-0 fst-italic">
                                        Read more
                                    </a>
                                </div>
                            </div>
                        </div>
                                                
                                                <div class="col-lg-4 col-md-6 col-12 mb-5">
                            <div class="row">
                                <div class="col-5">
                                    <div class="member-img">
                                        <img class=" img-fluid" src="images/team/sandeep.jpeg">
                                    </div>
                                </div>
                                <div class="col organizers_details">
                                                                            <a class="name" href="team/sandeep-kumar-srivastava">Mr. Sandeep Kumar Srivastava</a>
                                    <p class="title">Team Lead of Data Management</p>
                                    <div class="social_links">
                                        <a href="https://linkedin.com/in/sandeep-srivastav-90b249189" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                                        <!--<a href="#"><i class="fa-solid fa-envelope"></i></a>-->
                                        <!--<a href="#"><i class="fa-brands fa-x-twitter"></i></a>-->

                                    </div>
                                    <p class="desc">
                                        
                                        As team lead of Data Management, he plays a pivotal role in overseeing data processes, ensuring data integrity, and guiding his team to optimize workflows. He is an accomplished leader ...                                    </p>
                                    <a href="team/sandeep-kumar-srivastava" class="view-btn fs-6 p-0 fst-italic">
                                        Read more
                                    </a>
                                </div>
                            </div>
                        </div>
                                                
                                                
                    </div>
                </div>
            </div>
            <div class="text-center">
                <a href="team" class="view-btn">
                    View all Team
                </a>
            </div>
            <br>

            
        </div>
    </section>
    <!-- Our organizers sections end -->
    <section class="our-brands-section wrapper">
        <div class="heading">
            <h2 class="text-auto">
                Our Brands
            </h2>
        </div>
        <div class="container logo-slider">
            <div class="owl-carousel">
                <a href="https://ecowebinarupdate.com" target="_blank"> <img src="images/brands/ecowebinar.png" class="img-fluid">
                </a>
                <a href="https://conferencepanel.com" target="_blank"> <img src="images/brands/conferencepanel.webp" class="img-fluid">
                </a>
                <a href="https://humaanized.com" target="_blank"> <img src="images/brands/humaanized.png" class="img-fluid">
                </a>
                <a href="https://ineducator.com" target="_blank"> <img src="images/brands/ineducator.png" class="img-fluid">
                </a>
                <a href="https://onlineaudiowebinar.com" target="_blank"> <img src="images/brands/oaw.png" class="img-fluid">
                </a>
                <a href="https://profeducations.com" target="_blank"> <img src="images/brands/proeducation.png" class="img-fluid">
                </a>
                <a href="https://webinarplaneur.com" target="_blank"> <img src="images/brands/webinarplaneur.png" class="img-fluid">
                </a>
            </div>
        </div>
    </section>
    

    <!-- our speaker start -->
    <section class="speakers-section" style="display:none;">
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2 class="ms-3">
                    Our Speakers
                </h2>
            </div>
            <div class="row mx-2 row-gap-5">
                <div class="col-lg-3 col-12  ">
                    <p>At aabhyasa, we are proud to feature a diverse lineup of speakers who are leaders and innovators in their respective fields. Our speakers bring a wealth of knowledge, experience, and passion to the topics they cover, ensuring that every event is both informative and inspiring.</p>
                    <br>
                    <p>Our speakers have participated in numerous high-profile events, sharing their expertise on topics such as:</p>
                    <div class="our-speaker">
                        <ul>
                            <li><strong>Industry Pioneers</strong></li>
                            <li><strong>Thought Leaders</strong></li>
                            <li><strong>Innovators and Entrepreneurs</strong></li>
                            <li><strong>Educators and Researchers</strong></li>
                        </ul>
                    </div>
                    <a class="fill-btn my-3" data-bs-toggle="modal" data-bs-target="#speaker-opportunity-modal">Apply to Speak!</a>

                </div>
                <div class="col-lg-9  ps-lg-5">
                    <div class="row">
                                                    <div class="col-sm-10 col-md-6 mb-5">
                                <div class="row">
                                    <div class="col-5">
                                        <img class="rounded-2 img-fluid" src="https://conferencepanel.com/dashboard/public/speakers/unnamed_1690437113.jpg" alt="Pauline Sanders">
                                    </div>
                                    <div class="col organizers_details">
                                        <a class="name">Pauline Sanders</a>
                                        <p class="title">RN, MBA, CPHRM, LNCC, CCM</p>
                                        <div class="social_links">
                                            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                                            <a href="#"><i class="fa-solid fa-envelope"></i></a>
                                            <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                                        </div>
                                        <p class="desc">Pauline has over 25 years of experience in Healthcare Quality Management, which includes risk management and legal nurse consulting. She has directed and managed clinical risk mana</p>
                                        <a href="#" style="float: right;"><i>Read More</i></a>
                                    </div>
                                </div>
                            </div>
                                                    <div class="col-sm-10 col-md-6 mb-5">
                                <div class="row">
                                    <div class="col-5">
                                        <img class="rounded-2 img-fluid" src="https://conferencepanel.com/dashboard/public/speakers/02_EU_OSATO_Shot_2_242C_1709620882.jpg" alt="Osato F. Chitou">
                                    </div>
                                    <div class="col organizers_details">
                                        <a class="name">Osato F. Chitou</a>
                                        <p class="title">Esq., MPH</p>
                                        <div class="social_links">
                                            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                                            <a href="#"><i class="fa-solid fa-envelope"></i></a>
                                            <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                                        </div>
                                        <p class="desc">Osato F. Chitou, Esq., MPH&nbsp;is an attorney by training, however, before finding the law and compliance was both an educator and a social worker. These experiences have allowed </p>
                                        <a href="#" style="float: right;"><i>Read More</i></a>
                                    </div>
                                </div>
                            </div>
                                                    <div class="col-sm-10 col-md-6 mb-5">
                                <div class="row">
                                    <div class="col-5">
                                        <img class="rounded-2 img-fluid" src="https://conferencepanel.com/dashboard/public/speakers/Susan-Strauss200_1647416383.png" alt="Susan Strauss">
                                    </div>
                                    <div class="col organizers_details">
                                        <a class="name">Susan Strauss</a>
                                        <p class="title">Workplace, School Harassment &</p>
                                        <div class="social_links">
                                            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                                            <a href="#"><i class="fa-solid fa-envelope"></i></a>
                                            <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                                        </div>
                                        <p class="desc">Dr. Susan Strauss&nbsp;is a national and international consultant, speaker, and trainer in organizational effectiveness and management development. She has established numerous onb</p>
                                        <a href="#" style="float: right;"><i>Read More</i></a>
                                    </div>
                                </div>
                            </div>
                                                    <div class="col-sm-10 col-md-6 mb-5">
                                <div class="row">
                                    <div class="col-5">
                                        <img class="rounded-2 img-fluid" src="https://conferencepanel.com/dashboard/public/speakers/Dr-Mackles-MD-MBA-LHRM_1681277623.jpg" alt="Arnold Mackles">
                                    </div>
                                    <div class="col organizers_details">
                                        <a class="name">Arnold Mackles</a>
                                        <p class="title">MD, MBA</p>
                                        <div class="social_links">
                                            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                                            <a href="#"><i class="fa-solid fa-envelope"></i></a>
                                            <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                                        </div>
                                        <p class="desc">Dr. Mackles practiced hospital-based neonatal medicine in Florida for over twenty-two years after completing a Pediatric Residency at Lenox Hill Hospital in New York City, and a Fe</p>
                                        <a href="#" style="float: right;"><i>Read More</i></a>
                                    </div>
                                </div>
                            </div>
                                            </div>
                    <div class="text-md-end text-center">
                        <a href="speakers" class="view-btn text-black">
                            View all
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- our speaker end -->

    <!-- ondemand form section start -->
    <section class="ondemand-section" style="display:none;">
        <div class="container wrapper">
            <div class="row mx-2">
                <div class="col-lg-8 col-md-10 col-12 mx-auto text-center">
                    <h2>webinar on-demand</h2>
                    <p>Dive into the world of personalized webinars available nationwide! Suggest your topic, specify the number of attendees, and let us handle the rest. We will ensure a seamless and impactful virtual session for your organization.</p>

                    <a class="main-btn" data-bs-toggle="modal" data-bs-target="#on-demand-modal">Make a Request</a>
                </div>
            </div>
        </div>
    </section>
    <!-- ondemand form section end -->

    <!-- live events secion start -->
    <section class="events" style="display:none;">
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2 class="ms-3">
                    Live Schedule
                </h2>
            </div>

            <div class="row mx-2 row-gap-5">
                                    <div class="col-12">
                        <div class="event-box">
                            <div class="row row-gap-2">
                                <div class="col-lg-2 col-12">
                                    <h3 class="date">05 Mar 2025</h3>

                                    <p class="speaker">Michael Strong</p>
                                </div>
                                <div class="col-lg-8 col-md-10 col-12">
                                    <div class="event-details">
                                        <span class="industry">MEDICAL BILLING CODING WEBINARS</span> &vert;
                                        <span class="time">11:00 AM EST</span> &vert;
                                        <span class="duration">90 MINUTES</span>

                                        <h3>Mastering Pathology and Lab Coding Updates 2025: Stay Ahead in Co...</h3>
                                        <p><p>As of 2025, there are more than 100 new codes, almost 20 deletions, and approximately 10 revisions for pathology and laboratory CPT codes. However, the bulk of these are all related to Proprietary Laboratory...</p>
                                    </div>
                                </div>
                                <div class="col-md-1 col-12 text-end text-lg-center my-auto">
                                    <a href="https://conferencepanel.com/conference/mastering-pathology-and-lab-coding-updates-2025" class="main-btn " target="_blank">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                                    <div class="col-12">
                        <div class="event-box">
                            <div class="row row-gap-2">
                                <div class="col-lg-2 col-12">
                                    <h3 class="date">11 Mar 2025</h3>

                                    <p class="speaker">Lyman G. Sornberger</p>
                                </div>
                                <div class="col-lg-8 col-md-10 col-12">
                                    <div class="event-details">
                                        <span class="industry">MEDICAL BILLING CODING WEBINARS</span> &vert;
                                        <span class="time">11:30 AM EST</span> &vert;
                                        <span class="duration">60 MINUTES</span>

                                        <h3>Revenue Integrity and Charge Capture</h3>
                                        <p><p><strong>Ensuring That All of Your Hard Work Is Accounted for And Captured</strong></p>

<ul>
	<li>Making Sure All Services Are Billed Correctly
	<ul>
		<li>Why It Matters: It&#39;s important to make sur...</p>
                                    </div>
                                </div>
                                <div class="col-md-1 col-12 text-end text-lg-center my-auto">
                                    <a href="https://conferencepanel.com/conference/revenue-integrity-and-charge-capture" class="main-btn " target="_blank">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                                    <div class="col-12">
                        <div class="event-box">
                            <div class="row row-gap-2">
                                <div class="col-lg-2 col-12">
                                    <h3 class="date">18 Mar 2025</h3>

                                    <p class="speaker">Melveen Stevenson</p>
                                </div>
                                <div class="col-lg-8 col-md-10 col-12">
                                    <div class="event-details">
                                        <span class="industry">HUMAN RESOURCES</span> &vert;
                                        <span class="time">12:00 PM EST</span> &vert;
                                        <span class="duration">60 MINUTES</span>

                                        <h3>Unmasking the Crisis - Tackling the Epidemic of Violence in Healt...</h3>
                                        <p><p>In the healthcare industry, workplace violence has become a silent epidemic, posing significant risks to the safety and well-being of healthcare professionals. This&nbsp; 60-minute session aims to shed light...</p>
                                    </div>
                                </div>
                                <div class="col-md-1 col-12 text-end text-lg-center my-auto">
                                    <a href="https://conferencepanel.com/conference/unmasking-the-crisis-tackling-the-epidemic-of-violence-in-healthcare-workplaces" class="main-btn " target="_blank">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                                    <div class="col-12">
                        <div class="event-box">
                            <div class="row row-gap-2">
                                <div class="col-lg-2 col-12">
                                    <h3 class="date">11 Apr 2025</h3>

                                    <p class="speaker">Dr. Irina Koyfman</p>
                                </div>
                                <div class="col-lg-8 col-md-10 col-12">
                                    <div class="event-details">
                                        <span class="industry">MEDICAL BILLING CODING WEBINARS</span> &vert;
                                        <span class="time">1:00 PM EST</span> &vert;
                                        <span class="duration">60 MINUTES</span>

                                        <h3>Mastering CCM: Best Practices for Patient Engagement, Workflow Ef...</h3>
                                        <p><p>Chronic Care Management (CCM) continues to be one of the most impactful programs for improving patient outcomes and generating sustainable revenue for healthcare practices. However, <strong>engaging patients...</p>
                                    </div>
                                </div>
                                <div class="col-md-1 col-12 text-end text-lg-center my-auto">
                                    <a href="https://conferencepanel.com/conference/mastering-ccm-best-practices-for-patient-engagement-workflow-efficiency-and-maximizing-reimbursement" class="main-btn " target="_blank">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                            </div>

        </div>
    </section>

    <!-- live events secion end -->

    <!-- subscribe section start-->
    <section class="subscribe-section">
        <ul class="circles">
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
        </ul>
        <div class="container wrapper">
            <div class="row  align-items-center">
                <div class="col-md-5 text-md-end text-center pe-md-3 border-end border-2 py-3">
                    <h2 class="">Subscribe</h2>
                    <p class="">Now, to get updates!</p>
                </div>
                <div class="col-md-7 col-12 ps-md-5 ps-0 text-md-start text-center">
                    <form action="save-form.php?frm=subscribe" method="POST">
                        <label for="">
                            <input type="email" name="email" id="email" oninput="validateEmailSubscribe(this)" placeholder="Enter email..." required>
                        </label>
                        
                        <button type="submit" name="submitSubscription" id="submitSubscription" class="fill-btn">Subscribe</button>
                    </form>
                    <span id="alertMessageEmailSubscribe" style="color: red; display: none;">Enter a valid email!</span>
                </div>
            </div>
        </div>
    </section>
    <!-- subscribe section end-->

    <!-- recorded events start  -->
    <section class="events" style="display:none;">
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2 class="ms-3">
                    Past Events
                </h2>
            </div>
            <div class="row mx-2 row-gap-5">
                            </div>
        </div>
    </section>
    <!-- recorded events end  -->

    <!-- sponsers section start -->
    <section class="logo-section">
        <div class="container-fluid wrapper">
            <div class="heading ">
                <h2 class="mx-auto mb-5">
                    Get Certified
                </h2>
            </div>
            <div class="row mx-2 row-gap-3 mt-4">
                <div class="col-lg-2  col-sm-4 col-6">
                    <div class="card">
                        <img src="images/certificate/aapc.png" alt="">
                    </div>
                </div>
                <div class="col-lg-2  col-sm-4 col-6">
                    <div class="card">
                        <img src="images/certificate/ahima.png" alt="">
                    </div>
                </div>
                <div class="col-lg-2  col-sm-4 col-6">
                    <div class="card">
                        <img src="images/certificate/ancc.png" alt="">
                    </div>
                </div>
                <div class="col-lg-2  col-sm-4 col-6">
                    <div class="card">
                        <img src="images/certificate/BCEN.png" alt="">
                    </div>
                </div>
                <div class="col-lg-2  col-sm-4 col-6">
                    <div class="card">
                        <img src="images/certificate/hrci.png" alt="">
                    </div>
                </div>
                <div class="col-lg-2  col-sm-4 col-6">
                    <div class="card">
                        <img src="images/certificate/SHRM.png" alt="">
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- sponsers section end -->


    <!-- contact section start -->
    <!--<section class="contact-section">-->
    <!--    <div class="container-fluid ">-->
    <!--        <div class="row">-->
    <!--            <div class="col-md-6 col-12">-->
    <!--                <div class="contact-box">-->
    <!--                    <div class="heading">-->
    <!--                        <h2 class="ms-0">-->
    <!--                            Contact us-->
    <!--                        </h2>-->
    <!--                    </div>-->
    <!--                    <p>Need assistance or have questions? Feel free to contact us for support and inquiries. We are here to help!</p>-->

    <!--                    <div class="contact-info">-->
    <!--                       <p><i class="fa-solid fa-location-dot"></i>-->
	   <!--                 <b>USA 1 : &nbsp;</b><a href=""> 8 The Green, STE A, Dover, DE-19901</a>-->
	   <!--             </p>-->
	   <!--             <p><i class="fa-solid fa-location-dot"></i>-->
	   <!--                 <b>USA 2 : &nbsp;</b><a href=""> 1 Auer CT East, Brunswick, New Jersey-08816</a>-->
	   <!--             </p>-->
	   <!--             <p><i class="fa-solid fa-phone-volume"></i>-->
	   <!--                 <a href="tel:+13023634845"><b> Phone Number(USA) : &nbsp;</b>+1 (302) 363-4845</a>-->
	   <!--             </p>-->
	
	   <!--             <p><i class="fa-solid fa-location-dot"></i>-->
	   <!--                 <a href=""><b> India : &nbsp;</b> 4th floor, Kuber Complex, Rathyatra, Varanasi, UP-221010</a>-->
	   <!--             </p>-->
	   <!--             <p><i class="fa-solid fa-phone-volume"></i>-->
	   <!--                 <a href="tel:+919628442255"><b> Phone Number(India) : &nbsp;</b>+91 9628442255</a>-->
	   <!--             </p>-->
	   <!--             <p><i class="fa-solid fa-envelope"></i>-->
	   <!--                 <b>Email: &nbsp;</b><a href="mailto:info@aabhyasa.com" style="text-transform: lowercase;"> info@aabhyasa.com</a>-->
	   <!--             </p>-->

    <!--                    </div>-->
    <!--                    <div class="social-links">-->
    <!--                        <a href=""><i class="fa-brands fa-facebook"></i></a>-->
    <!--                        <a href=""><i class="fa-brands fa-x-twitter"></i></a>-->

    <!--                        <a href="https://www.linkedin.com/company/aabhyasa-technologies-pvt-ltd/mycompany/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>-->

    <!--                    </div>-->

    <!--                </div>-->
    <!--            </div>-->
    <!--            <div class="col-md-6 col-12 contact-form">-->
    <!--                <ul class="circles">-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                    <li></li>-->
    <!--                </ul>-->
    <!--                <form action="save-form.php?frm=contact" method="POST">-->
    <!--                    <div class="form-control">-->
    <!--                        <input type="text" id="name" name="name" oninput="validateInput(this)" required>-->
    <!--                        <label> Name </label>-->
    <!--                        <span id="alertMessageName" style="color: red; display: none;">Only alphanumeric characters are allowed!</span>-->
    <!--                    </div>-->
    <!--                    <div class="form-control">-->
    <!--                        <input type="email" id="email" name="email" oninput="validateEmail(this)" required>-->
    <!--                        <label> Email </label>-->
    <!--                        <span id="alertMessageEmail" style="color: red; display: none;">Invalid email input, Please enter a valid email!</span>-->
    <!--                    </div>-->
    <!--                    <div class="form-control">-->
    <!--                        <input type="text" id="phone" name="phone" oninput="validatePhoneNumber(this)" required>-->
    <!--                        <label> Phone </label>-->
    <!--                        <span id="phoneAlertMessage" style="color: red; display: none;">Invalid phone number. Please enter a valid phone number.</span>-->
    <!--                    </div>-->
    <!--                    <div class="form-control">-->
    <!--                        <textarea name="message" id="message" rows="4" oninput="validateInput(this)" rows="5"></textarea>-->
    <!--                        <label> Your Message </label>-->
    <!--                        <span id="alertMessageText" style="color: red; display: none;">Only alphanumeric characters are allowed!</span>-->
    <!--                    </div>-->
    <!--                    <input type="hidden" id="subject" name="subject" value="Received from Homepage" oninput="validateInput(this)" required>-->
    <!--                    <button class="fill-btn" type="submit" id="submit">Submit</button>-->

    <!--                </form>-->
    <!--            </div>-->
    <!--        </div>-->
    <!--    </div>-->
    <!--</section>-->
    <!-- contact section end -->

    <!-- why us section start -->
    <section class="why-us">
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2 class="mx-auto">
                    Why choose us
                </h2>
            </div>
            <div class="row mx-2 row-gap-3 benefits">
                <div class="col-lg-3 col-md-6 col-12">
                    <div class="benefits-item">
                        <img src="images/whyus-img/asset.png" alt="">
                        <h4>Enhance Your Value</h4>
                        <p>Healthy, knowledgeable employees are among a company's greatest assets. Stay ahead in your profession by acquiring the most up-to-date knowledge and becoming an invaluable resource to your organization.</p>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-12">
                    <div class="benefits-item">
                        <img src="images/whyus-img/custom.png" alt="why us image">
                        <h4>Tailored Solutions</h4>
                        <p>Our solutions go beyond standard education. We provide personalized learning experiences customized to meet your specific professional needs and career goals, ensuring you gain relevant, actionable insights.</p>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-12">
                    <div class="benefits-item">
                        <img src="images/whyus-img/savings.png" alt="why us image">
                        <h4>Cost-Effective Insights</h4>
                        <p>With our fully online sessions, you save on travel and accommodation costs. All you need is a reliable internet connection, making our programs both convenient and budget-friendly.</p>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-12">
                    <div class="benefits-item">
                        <img src="images/whyus-img/career.png" alt="why us image">
                        <h4>Stay Ahead of the Curve</h4>
                        <p>We keep you updated with the latest industry developments and contemporary changes, ensuring you remain competitive and equipped with cutting-edge knowledge in an ever-evolving market.</p>
                    </div>
                </div>
            </div>


            <div class="row text-center my-5 px-4 row-gap-5 mx-0 increamenting-numbers">
                <div class="col-lg-4 col-md-6 col-12 mb-2">
                    <h1><span class="number-animate" data-end-value="10" data-increment="1" data-duration="2000">0</span>+</h1>
                    <span>Countries</span>
                </div>
                <div class="col-lg-4 col-md-6 col-12 mb-2">
                    <h1><span class="number-animate" data-end-value="900" data-increment="100" data-duration="2000">0</span>+</h1>
                    <span>Webinars
                    </span>
                </div>
                <div class="col-lg-4 col-md-6 col-12 mb-2">
                    <h1><span class="number-animate" data-end-value="33370" data-increment="500" data-duration="2000">0</span>+</h1>
                    <span>Customers
                    </span>
                </div>
                <!--<div class="col-lg-3 col-md-6 col-12 mb-2">-->
                <!--    <h1><span class="number-animate" data-end-value="3052" data-increment="109" data-duration="2000">25</span>+</h1>-->
                <!--    <span>Delivered-->
                <!--    </span>-->
                <!--</div>-->
            </div>
        </div>
    </section>
    <!-- why us section end -->

    <!-- faq section start -->
    <section class="faq-section">
        <div class="container-fluid wrapper">
            <div class="heading">
                <h2 class="ms-3">
                    FAQs
                </h2>
            </div>
            <div class="row mx-2">
                <div class="col-md-7 col-12">
                    <details class="accordion" open>
                        <summary class="accordion__title">
                            <span class="accordion__marker"></span> When and how will I receive information on how to participate in a live webinar?
                        </summary>
                        <div class="accordion__content">
                            <p>You will receive all the details of the live webinar 48 hours before the scheduled session. This includes dial-in instructions, the link, and password for accessing the webinar, as well as any handouts and related materials. You can download these from the webinar page at www.aabhyasa.com. If you don't see the email, please check your spam or junk folder.</p>
                        </div>
                    </details>
                    <details class="accordion">
                        <summary class="accordion__title">
                            <span class="accordion__marker"></span> How do I register for a webinar? 
                        </summary>
                        <div class="accordion__content">
                            To register for a webinar, visit our website, select the webinar you're interested in, and complete the registration form. Once your registration is complete, you will receive a confirmation email with further details.
                        </div>
                    </details>
                    <details class="accordion">
                        <summary class="accordion__title">
                            <span class="accordion__marker"></span>Can I ask questions during the webinar? 
                        </summary>
                        <div class="accordion__content">
                            Yes, our webinars include interactive Q&A sessions where you can ask questions and engage with the speakers. This is an excellent opportunity to gain deeper insights and clarify any doubts you may have.
                        </div>
                    </details>
                </div>

            </div>
        </div>
    </section>
    <!-- faq section end -->

    <footer>
    <div class="container-fluid wrapper">
        <div class="text-center pb-4 mb-5 border-bottom">
            <a href="index" class="logo">
                <img src="images/aabhyasa_logo_element.png" alt="" class="img-fluid">aabhyasa
            </a>
        </div>
        <div class="row mx-2 row-gap-5 py-5">
            <div class="col-lg-4 col-md-4 col-12">
                <h4>Reach us</h4>              
                <p><i class="fa-solid fa-location-dot"></i>
                    <b>USA 1 : &nbsp;</b><a href=""> 8 The Green, STE A, Dover, DE-19901</a>
                </p>
                <p><i class="fa-solid fa-location-dot"></i>
                    <b>USA 2 : &nbsp;</b><a href=""> 1 Auer CT East, Brunswick, New Jersey-08816</a>
                </p>
                <p><i class="fa-solid fa-phone-volume"></i>
                    <a href="tel:+13023634845"><b>Phone Number (USA) : &nbsp;</b>+1 (302) 363-4845</a>
                </p>

                <p><i class="fa-solid fa-location-dot"></i>
                    <a href=""><b>India : &nbsp;</b>4th floor, Kuber Complex, Rathyatra, Varanasi, UP-221010</a>
                </p>
                <p><i class="fa-solid fa-phone-volume"></i>
                    <a href="tel:+919628442255"><b>Phone Number (India) : &nbsp;</b>+91 7388172255</a>
                </p>
                <p><i class="fa-solid fa-envelope"></i>
                                     <b>Email: &nbsp;</b><a href="mailto:info@aabhyasa.com" style="text-transform: lowercase;">info@aabhyasa.com</a>
                                    </p>

            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                <h4>Company</h4>
                <p><a href="about">About us</a></p>
                <p><a href="team">Leadership</a></p>
                <!--<p><a href="speakers">Speakers</a></p>-->
                <p><a href="career">Careers <span>we are hiring</span></a></p>
                <p><a href="contact">Contact Us</a></p>
                <p><a href="faq">FAQs</a></p>

            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                <h4>Important Links</h4>
                <p><a href="privacy-policy">Privacy Policy</a></p>
                <p><a href="terms">Terms & conditions</a></p>
                <p><a href="refund">Refund Policy</a></p>
                <p><a data-bs-toggle="modal" data-bs-target="#speaker-opportunity-modal">Speaker Opportunity</a></p>
                <p><a data-bs-toggle="modal" data-bs-target="#on-demand-modal">On-demand webinar</a></p>
                <!--<p><a href="unsubscribe">Unsubscribe</a></p>-->
            </div>
            <div class="col-lg-4 col-md-12 col-12 ps-lg-5 ps-0">
                <div class="row mx-0 row-gap-3">
                    <div class="col-lg-12 col-md-6 col-12">
                        <h4>Get in Touch</h4>
                        <div class="signup_form">
                            <form action="#" class="subscribe">
                                <input type="text" class="subscribe__input" placeholder="Enter Email Address">
                                <button type="button" class="subscribe__btn"><i class="fas fa-paper-plane"></i></button>
                            </form>
                        </div>
                    </div>
                    <div class="col-lg-12 col-md-6 col-12 text-md-end text-start text-lg-start">
                        <!-- social icons -->
                        <div class="social-icons my-lg-5 my-3">
                            <a href="https://www.facebook.com/aabhyasa/" target="_blank"><i class="fa-brands fa-facebook-f"></i></a>
                            <!--<a href=""><i class="fa-brands fa-x-twitter" target="_blank"></i></a>-->
                            <!--<a href=""><i class="fa-brands fa-pinterest-p" target="_blank"></i></a>-->
                            <a href="https://www.linkedin.com/company/aabhyasa-technologies-pvt-ltd/mycompany/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>
                            <!--<a href="" target="_blank"><i class="fa-brands fa-youtube"></i></a>-->

                        </div>
                        <!-- payment icons -->
                        <div class="payment-options">
                            <span>
                                <span href="">
                                    <img src="images/payment-icon/master-card.png" alt="" class="img-fluid">
                                </span>
                                <span href="">
                                    <img src="images/payment-icon/visa.png" alt="" class="img-fluid">
                                </span>
                                <span href="">
                                    <img src="images/payment-icon/maestro.png" alt="" class="img-fluid">
                                </span>
                                <span href="">
                                    <img src="images/payment-icon/american-express.png" alt="" class="img-fluid">
                                </span>
                                <span href="">
                                    <img src="images/payment-icon/paypal.png" alt="" class="img-fluid">
                                </span>
                            </span>
                        </div>
                    </div>
                </div>


            </div>
        </div>

    </div>
    <div class="footer-bottom">
        <span style="text-transform: lowercase;">© Aabhyasa Technologies Pvt. Ltd. , All rights reserved.</span>
    </div>
</footer>

<!-- On demand form modal  -->
<div class="modal fade " id="on-demand-modal" data-bs-backdrop="static" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header-div text-center">
                <img src="images/google-forms.png" alt="" class="img-fluid">
                <h2 class="modal-title" id="staticBackdropLabel">On-Demand Webinar</h2>
                <p>Discover how we can meet your compliance needs.</p>
                <a data-bs-dismiss="modal" aria-label="Close">
                    <i class="fa-solid fa-circle-xmark"></i>
                </a>
            </div>

            <div class="modal-body">
                <form action="save-form.php?frm=onDemand" method="POST">
                    <fieldset>
                        <div class="form-control">
                            <input type="text" name="nameOD" id="nameOD" oninput="validateInput(this)" required>
                            <label> Name </label>
                            <span id="alertMessageNameOD" style="color: red; display: none;">Only alphanumeric characters are allowed!</span>
                        </div>
                        <div class="form-control">
                            <input type="text" name="organizationOD" id="organizationOD" oninput="validateInput(this)" required>
                            <label> Organization </label>
                            <span id="alertMessageOrg" style="color: red; display: none;">Only alphanumeric characters are allowed!</span>
                        </div>
                        <div class="form-control">
                            <input type="text" name="topicOD" id="topicOD" oninput="validateInput(this)" required>
                            <label> Topic </label>
                            <span id="alertMessageTopic" style="color: red; display: none;">Only alphanumeric characters are allowed!</span>
                        </div>
                        <div class="form-control">
                            <input type="text" name="phoneOD" id="phoneOD" oninput="validatePhoneNumber(this)" required>
                            <label> Phone </label>
                            <span id="phoneAlertMessage" style="color: red; display: none;">Invalid phone number. Please enter a valid phone number.</span>
                        </div>
                    </fieldset>
                    <div class="cta my-3">
                        <button type="submit" name="submit" id="submit" class="submit-btn d-block">Submit Request</button>
                        <a href="mailto:info@aabhyasa.com" target="_blank" class="main-btn d-block mt-3"><i class="fa-solid fa-phone-volume"></i>
                            Quick Contact</a>
                    </div>
                </form>
                <p class="fs-6">Our Business Development Team will get in touch with you within
                    24 business hours
                </p>
            </div>

        </div>
    </div>
</div>
<!-- On demand form modal  end-->

<!-- speaker-opportunity form modal  -->
<div class="modal fade " id="speaker-opportunity-modal" data-bs-backdrop="static" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header-div text-center">
                <img src="images/speaker-form.png" alt="" class="img-fluid">
                <h3 class="modal-title" id="staticBackdropLabel">Opportunity To Be A Part Of Our Expert Panel</h3>
                <p>Just fill out this simple form below, and soon you will hear from us!</p>
                <a data-bs-dismiss="modal" aria-label="Close">
                    <i class="fa-solid fa-circle-xmark"></i>
                </a>
            </div>

            <div class="modal-body">
                <fieldset>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Name </label>
                    </div>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Job Title </label>
                    </div>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Phone </label>
                    </div>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Company </label>
                    </div>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Fax </label>
                    </div>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Email </label>
                    </div>
                    <div class="form-control">
                        <input type="text" required>
                        <label> Industry </label>
                    </div>
                </fieldset>
                <div class="cta my-3">
                    <a class="submit-btn d-block">Submit Request</a>
                    <a href="callto:+1234567890" class="main-btn d-block mt-3"><i class="fa-solid fa-phone-volume"></i>
                        Quick Call</a>
                </div>
                <p class="fs-6">Our Business Development Team will get in touch with you within
                    24 business hours
                </p>
            </div>

        </div>
    </div>
</div>
<!-- speaker-opportunity form modal  end-->

<script>
    function validateInput(input) {
            var regex = /^[a-zA-Z0-9 ]*$/;
            var goFor = input.id;
            console.log(goFor);
            var submitButton =document.getElementById('submit');
            switch (goFor) {
                case 'nameOD':
                    var alertMessage = document.getElementById('alertMessageNameOD');
                    break;
                case 'topicOD':
                    var alertMessage = document.getElementById('alertMessageTopic');
                    break;
                case 'organizationOD':
                    var alertMessage = document.getElementById('alertMessageOrg');
                    break;
                case 'name':
                    var alertMessage = document.getElementById('alertMessageName');
                    break;
                case 'subject':
                    var alertMessage = document.getElementById('alertMessageSubject');
                    break;
                case 'message':
                    var alertMessage = document.getElementById('alertMessageText');
                    break;
            
                default:
                    break;
            }
            if (!regex.test(input.value)) {
                alertMessage.style.display = 'inline';
                submitButton.disabled = true;
            } else {
                alertMessage.style.display = 'none';
                submitButton.disabled = false;
            }
        }
        function validateEmail(input) {
            var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            var alertMessage = document.getElementById('alertMessageEmail');
            var submitButton =document.getElementById('submit');
            if (!regex.test(input.value)) {
                alertMessage.style.display = 'inline';
                submitButton.disabled = true;
            } else {
                alertMessage.style.display = 'none';
                submitButton.disabled = false;
            }
        }

        function validateEmailSubscribe(input) {
            var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            var alertMessage = document.getElementById('alertMessageEmailSubscribe');
            var submitButtonS =document.getElementById('submitSubscription');
            if (!regex.test(input.value)) {
                alertMessage.style.display = 'inline';
                submitButtonS.disabled = true;
            } else {
                alertMessage.style.display = 'none';
                submitButtonS.disabled = false;
            }
        }

        function validatePhoneNumber(input) {
            var regex = /^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$|^(\+91[\-\s]?)?[6-9]\d{9}$/;
            var alertMessage = document.getElementById('phoneAlertMessage');
            var submitButton =document.getElementById('submit');
            if (!regex.test(input.value)) {
                alertMessage.style.display = 'inline';
                submitButton.disabled = true;
            } else {
                alertMessage.style.display = 'none';
                submitButton.disabled = false;
            }
        }
</script>
    <script src="assets/js/jquery-3.7.1.js"></script>

<!-- jQuery -->

<!-- Bootstrap 5 JS -->
<script src="	https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>

<!-- number animation js cdn -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>



<!-- custom js  -->
<script src="assets/js/script.js"></script>

<!-- Owl carousel js  -->
<script src="assets/js/owl.carousel.js"></script>
<script src="assets/js/owl.carousel.min.js"></script></body>

</html>
"""

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# url = "https://www.eversana.com/thought-leaders/?sf_paged=3"
# driver.get(url)
# html = driver.page_source
# driver.quit()

import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from groq import Groq

EXCLUDED_TAGS = {
    "header", "footer", "script", "style", "noscript", "nav", "iframe", 
    "input", "svg", "aside", "button", "link", "meta", "picture", 
    "source", "object", "embed", "param", "canvas", "map", "area", "figure",
    "img", "br", "hr", "i", "table"
}

class HtmlExtractor:
    def __init__(self, html):
        self.html = html
        self.extracted_data = []

    def extract_and_save_data(self):
        """Extracts structured data from HTML and stores it in `self.extracted_data`."""
        soup = BeautifulSoup(self.html, "html.parser")
        
        for tag in soup.find_all(EXCLUDED_TAGS):
            tag.decompose()

        def get_direct_text(tag):
            """Extracts direct text content from an HTML tag."""
            return tag.get_text(strip=True) if tag.string else ""

        def build_json(tag, parent_path=""):
            """Recursively constructs a structured JSON representation."""
            if not tag.name:
                return None

            if tag.name == "a" and not tag.has_attr("href"):
                return None
            
            current_path = f"{parent_path}.{tag.name}" if parent_path else tag.name
            
            children = [
                build_json(child, current_path) for child in tag.find_all(recursive=False)
            ]
            children = [child for child in children if child]
            
            if len(children) == 1:
                return children[0]
            
            if tag.name == "div" and any(isinstance(child, dict) and child.get("tag", "").endswith("div") for child in children):
                return children
            
            node = {"tag": current_path}
            
            if tag.name == "a" and tag.has_attr("href") and tag["href"] != "#":
                node["href"] = tag["href"]
            
            text = get_direct_text(tag)
            if text:
                node["text"] = text
            
            if children:
                node["children"] = children
            
            if not node.get("text") and not node.get("href") and not node.get("children"):
                return None
            
            if "children" in node and len(node) == 1:
                return node["children"]
            
            return node

        self.extracted_data = build_json(soup.body) if soup.body else []
        return self.extracted_data if isinstance(self.extracted_data, list) else [self.extracted_data]

    def process_extracted_data(self):
        """Processes the extracted data and returns the final structured output."""
        tag_data = {}

        def extract_tags(node):
            if isinstance(node, dict):
                tag_name = node.get("tag", "")
                
                if tag_name:
                    if tag_name not in tag_data:
                        tag_data[tag_name] = []
                    
                    tag_info = node.get("text", node.get("href", None))
                    if tag_info:
                        tag_data[tag_name].append(tag_info)
                
                if "children" in node:
                    for child in node["children"]:
                        extract_tags(child)
            
            elif isinstance(node, list):
                for item in node:
                    extract_tags(item)

        extract_tags(self.extracted_data)
        tag_data = {key: value for key, value in tag_data.items() if value}

        checked_keys = {key for key in tag_data.keys() if len({tuple(single_data) if isinstance(single_data, list) else single_data for single_data in tag_data[key]}) == 1}
        unique_keys = [key for key in tag_data.keys() if key not in checked_keys]

        return {key: tag_data[key] for key in unique_keys}

class DeepSeekExtractor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = Groq(api_key=self.api_key)

    def query_model(self, json_input):
        """Send JSON input to DeepSeek and get raw CSV output."""
        prompt = (
            "Extract structured data from this JSON input and return as raw CSV text with columns: "
            "Name, Email, Phone, Title, Social Link (if available).\n\n"
            f"{json.dumps(json_input, indent=2)}"
        )

        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="deepseek-r1-distill-llama-70b",
            temperature=0.2,
            max_tokens=2048
        )

        return response.choices[0].message.content if response else None

    def save_csv(self, csv_text, filename="extracted_data.csv"):
        """Save raw CSV text to a file."""
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(csv_text)

        print(f"Data saved to {filename}")

if __name__ == "__main__":
    API_KEY = "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"
    html_extractor = HtmlExtractor(html)
    extracted_data = html_extractor.extract_and_save_data()
    processed_data = html_extractor.process_extracted_data()

    deepseek_extractor = DeepSeekExtractor(API_KEY)
    csv_output = deepseek_extractor.query_model(processed_data)

    if csv_output:
        deepseek_extractor.save_csv(csv_output)
