import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import HelloWorld from '../HelloWorld.vue'

describe('HelloWorld', () => {
  it('renders properly', () => {
    const wrapper = mount(HelloWorld, { props: { msg: 'Hello Vitest' } })
    expect(wrapper.text()).toContain('Hello Vitest')
  })
}),
  describe('Math operations', () => {
    it('adds two numbers correctly', () => {
      expect(2 + 3).toBe(5)
      expect(-1 + 1).toBe(0)
      expect(0 + 0).toBe(0)
    })

    it('subtracts two numbers correctly', () => {
      expect(5 - 3).toBe(2)
      expect(3 - 5).toBe(-2)
      expect(0 - 0).toBe(0)
    })
  })
