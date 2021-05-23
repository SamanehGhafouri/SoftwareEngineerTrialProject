import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StatisticsResultComponent } from './statistics-result.component';

describe('StatisticsResultComponent', () => {
  let component: StatisticsResultComponent;
  let fixture: ComponentFixture<StatisticsResultComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StatisticsResultComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StatisticsResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
