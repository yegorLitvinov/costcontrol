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
  id?: number;
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

export interface Todo extends TimeStamped {
  id: number;
  text: string;
  completed: boolean;
}

export interface AccountsState {
  user: User;
}

export interface CostcontrolState {
  history: BalanceRecord[],
  spendingCategories: Category[],
  proceedCategories: Category[],
  spendingStatistics: CategoryStatistic[],
  proceedStatistics: CategoryStatistic[],
  filledMonthes: FilledMonthes,
}

export interface TodoState {
  entities: {
    [id: string]: Todo
  },
  orderedIds: number[];
}

export interface RootState {
  accounts: AccountsState;
  costcontrol: CostcontrolState;
  todo: TodoState;
}
