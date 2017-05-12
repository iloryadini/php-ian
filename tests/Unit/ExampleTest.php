<?php

namespace Tests\Unit;

use Tests\TestCase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testBasicTest()
    {
        $box = new Box(['cat', 'toy', 'torch']);

        $this->assertTrue($box->has('toy'));
        $this->assertFalse($box->has('ball'));
    }
}
