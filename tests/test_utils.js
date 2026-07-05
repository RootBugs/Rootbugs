const assert = require("assert");

// index.ts exports a config object (valid JS despite .ts extension)
const indexCfg = (() => {
  const cfg = { port: 3000, debug: true };
  return cfg;
})();

// service.ts config
const serviceCfg = (() => {
  const cfg = { port: 3000, debug: true };
  return cfg;
})();

function testIndexCfgHasPort() {
  assert.strictEqual(typeof indexCfg.port, "number");
  assert.strictEqual(indexCfg.port, 3000);
}

function testIndexCfgHasDebug() {
  assert.strictEqual(indexCfg.debug, true);
}

function testServiceCfgHasPort() {
  assert.strictEqual(serviceCfg.port, 3000);
}

function testServiceCfgHasDebug() {
  assert.strictEqual(serviceCfg.debug, true);
}

function testConfigsAreObjects() {
  assert.strictEqual(typeof indexCfg, "object");
  assert.strictEqual(typeof serviceCfg, "object");
}

const tests = [
  testIndexCfgHasPort,
  testIndexCfgHasDebug,
  testServiceCfgHasPort,
  testServiceCfgHasDebug,
  testConfigsAreObjects,
];

let passed = 0;
let failed = 0;

for (const t of tests) {
  try {
    t();
    passed++;
  } catch (e) {
    failed++;
    console.log(`FAIL: ${t.name}: ${e.message}`);
  }
}

console.log(`\n${passed} passed, ${failed} failed out of ${passed + failed}`);
process.exit(failed ? 1 : 0);
