export enum CategoryKind {
  Proceed = 'proceed',
  Spending = 'spending'
}

export interface Category {
  id: number;
  color: string;
  name: string;
  kind: CategoryKind;
  user: number;
}

export interface CategoryStatistic extends Category {
  total: number;
}

interface TimeStamped {
  created_at?: string;
  updated_at?: string;
}

export interface BalanceRecord extends TimeStamped{
  id: number;
  amount: number;
  category: number;
  comment: string;
}

export interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  token?: string;
}

export interface FilledMonthes {
  [year: number]: {
    [month: number]: boolean
  }
}

export interface AccountsState {
  user: User;
}

export interface CostcontrolState {
  historyOrderedIds: number[];
  historyEntities: { [id: number]: BalanceRecord}
  spendingCategoriesOrderedIds: number[];
  spendingCategoriesEntities: { [id: number]: Category };
  proceedCategoriesOrderedIds: number[];
  proceedCategoriesEntities: { [id: number]: Category };
  spendingStatistics: CategoryStatistic[];
  proceedStatistics: CategoryStatistic[];
  yearStatistics: YearStatistic[];
  filledMonthes: FilledMonthes;
}

export interface RootState {
  accounts: AccountsState;
  costcontrol: CostcontrolState;
}

interface ChartDataset {
  label: string;
  backgroundColor: string[] | string;
  data: number[] | { x: number, y: number }[];
  options?: any;
}

export interface ChartData {
  labels: string[] | number[];
  datasets: ChartDataset[];
}

export interface CategoryYearStatistics {
  total: number;
  month: number;
}

export interface YearStatistic extends CategoryYearStatistics {
  category__kind: string;
}

export interface PaginatedResults<T> {
  count: number;
  next: null | string;
  previous: null | string;
  results: T[];
}
