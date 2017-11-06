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

export interface BalanceRecord {
  id?: number;
  amount: number;
  category: number;
  comment: string;
  created_at?: string;
  updated_at?: string;
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

export interface RootState {
  user: User;
  history: BalanceRecord[],
  spendingCategories: Category[],
  proceedCategories: Category[],
  spendingStatistics: CategoryStatistic[],
  proceedStatistics: CategoryStatistic[],
  filledMonthes: FilledMonthes,
}
