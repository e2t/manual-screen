unit Controller;

{$MODE OBJFPC}
{$LONGSTRINGS ON}
{$ASSERTIONS ON}
{$RANGECHECKS ON}
{$BOOLEVAL OFF}

interface

procedure Run();
procedure MainFormInit();

implementation

uses
  ProgramInfo, GuiMainForm, ScreenCalculation, GuiHelper, Measurements,
  Classes, SysUtils;

procedure MainFormInit();
begin
  MainForm.Caption := GetProgramTitle;
end;

function CreateInputData(out InputData: TInputData): string;
const
  SIncorrectValue = ' - неправильное значение.';
var
  Value: Double;
begin
  InputData := Default(TInputData);
  Result := '';

  if MainForm.EditWidth.GetRealMinEq(Value, ToMm(MinWidth)) then
    InputData.Width := Mm(Value)
  else
    Exit('Ширина решетки' + SIncorrectValue);

  if MainForm.EditLength.GetRealMinEq(Value, ToMm(MinLength)) then
    InputData.Length := Mm(Value)
  else
    Exit('Длина решетки' + SIncorrectValue);

  if MainForm.EditGap.GetRealMin(Value, 0) then
    InputData.Gap := Mm(Value)
  else
    Exit('Прозор' + SIncorrectValue);
end;

function CreateOutput(const Scr: TManualScreen): string;
var
  Lines: TStringList;
begin
  Lines := TStringList.Create;
  Lines.Add(Format('Масса решетки %.0f кг', [Scr.Weight]));
  Lines.Add(Format('Количество профиля "3999" %d шт.',
    [Scr.ProfileNumber]));
  Lines.Add(Format('Длина профиля %.0f мм', [ToMm(Scr.ProfileLength)]));
  Lines.Add('');
  if Scr.ExternalWidth > MaxWidth then
    Lines.Add(Format(
      'Масса занижена при ширине решетки свыше %.0f мм.',
      [
      ToMm(MaxWidth)]));
  if Scr.Length > MaxLength then
    Lines.Add(Format(
      'Масса занижена при длине решетки свыше %.0f мм.',
      [
      ToMm(MaxLength)]));
  Result := Lines.Text;
  Lines.Free;
end;

procedure PrintOutput(const Text: string);
begin
  MainForm.MemoOutput.Clear;
  MainForm.MemoOutput.Text := Text;
  MainForm.MemoOutput.SelStart := 0;
end;

procedure Run();
var
  InputData: TInputData;
  InputDataError: string;
  Scr: TManualScreen;
begin
  InputDataError := CreateInputData(InputData);
  if InputDataError = '' then
  begin
    CalcManualScreen(Scr, InputData);
    PrintOutput(CreateOutput(Scr));
  end
  else
    PrintOutput(InputDataError);
end;

end.
