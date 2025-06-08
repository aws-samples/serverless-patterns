module.exports = {
  testEnvironment: 'node',
  roots: ['<rootDir>/test'],
  testMatch: ['**/*.test.ts'],
  transform: {
    '^.+\\.tsx?$': 'ts-jest'
  },
  moduleNameMapper: {
    '^@ordersCommonCode/(.*)$': '<rootDir>/lib/ordersCommonCode/$1'
  },
  globals: {
    'ts-jest': {
      tsconfig: 'test/tsconfig.json'
    }
  }
};